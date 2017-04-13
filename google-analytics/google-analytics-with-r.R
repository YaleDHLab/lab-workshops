# googleAnalyticsR home page: http://code.markedmondson.me/googleAnalyticsR/
# A great intro to the package: http://www.dartistics.com/api-google-analytics.html

##
# Load dependencies
##

# Install the google analytics package if it isn't installed
if(!require(googleAnalyticsR)) install.packages("googleAnalyticsR")

# Load the googleAnalyticsR library
library(googleAnalyticsR)

##
# Authenticate with Google
##

# Grant the application access to your analytics data
ga_auth()

# The line above produces a .httr-oauth token that has
# Access to your GA data, so protect this file!

# To see the token, submit an 'ls' call to the operating system
system('ls -lsah')

##
# Querying Google Analytics
##

# In the GA world, a "view id" uniquely identifies a GA account
# you've configured for a website.

# After you've created a website and added GA to that site,
# you can access the view id for that site by visiting:
# https://ga-dev-tools.appspot.com/query-explorer/

view_id <- 112951844

# Pull the last 60 days of data for that view:
gadata <- google_analytics_4(view_id, 
                             date_range = c(Sys.Date() - 60, Sys.Date()),
                             metrics = 'sessions', 
                             dimensions = c('date','hour'),
                             max = -1)

# To review the documentation on the function we just ran:
?google_analytics_4

# An alternative way to get documentation
help(google_analytics_4)

# You can also search available documentation
help.search('Google Analytics')

# Show the first few rows from the returned object
head(gadata)

# Find the sum total of users from those days
sum(gadata$sessions)

##
# Some r indexing
##

# Get the first column of the matrix by its index position (R uses 1-based indexing)
gadata[[1]]

# Get the first column of the matrix by its column name
gadata$date

##
# Generate sample data with the shape of gadata object
##

# Select a number of observations to simulate; each observation is an hour
n.observations <- 7000

# Take 1000 samples of years between 2016 and 2017, with replacement
years <- sample( seq(2016, 2017), n.observations, replace=TRUE)

# Take 1000 samples of months between 1 and 12, with replacement
months <- sample( seq(1, 12), n.observations, replace=TRUE)

# Take 1000 samples of days between 1 and 28, with replacement
days <- sample( seq(1, 28), n.observations, replace=TRUE)

# Create a collection of dates by joining the year, month, and day values together
sample.dates <- as.Date( paste(years, months, days, sep='-'))

# Create a series of 1000 sample hours between 0 and 23
hours <- sample( seq(0, 23), n.observations, replace=TRUE)

# Create a series of 1000 integers to simulate user sessions
sessions <- rpois(n.observations, lambda = 10000)

# Create a dataframe with the following colums: date, hour, sessions
# This dataframe has the same structure as the gadata object returned by
# the google_analytics_4 function call above
gadata <- data.frame( date=sample.dates, hour=hours, sessions=sessions)

# Sort the dataframe by date; this is purely aesthetic
gadata <- gadata[do.call(order, gadata[c('date')]), ]

# Identify the day of the week on which each observation occurred
gadata$weekday <- weekdays(gadata$date)

# For each session observation in the sorted list, add 0.02 * the index
# position of the given observation to that observation's value to introduce
# a pattern into the data
gadata$sessions <- gadata$sessions +
                    (0.02 * seq_along(gadata$sessions)) +
                    (50 * as.integer(as.factor(gadata$weekday)))

##
# Prepare heatmap
##

# Install required packages:
#  - tidyr is for data manipulation
#  - highcharter is a wrapper for the highcharts plotting library
if(!require(tidyr)) install.packages("tidyr")
if(!require(highcharter)) install.packages("highcharter")

# Load the required packages
library(dplyr)
library(tidyr)
library(highcharter)

# Get a list of the days of the week in order
weekdays <- c('Monday', 'Tuesday', 'Wednesday', 'Thursday',
              'Friday', 'Saturday', 'Sunday')

# Add a day of the week to each observation in the dataframe
gadata$weekday <- ordered(weekdays(gadata$date), levels=weekdays)

# Create a subset of the gadata object that contains only the
# weekday, hour, and sessions columns
heatmap_data <- select(gadata, weekday, hour, sessions)

# Use the sum function to aggregate the total number of sessions
# for each weekday+hour combination in heatmap_data
heatmap_sums <- aggregate( sessions ~ 
                 weekday + hour,
                 sum,
                 data=heatmap_data)

# Push the data into the format required by highcharts ->
# each column will be an hour and each row a day of the week
heatmap_recast <- spread(heatmap_sums, hour, sessions)

# Make this "data frame" into a "matrix";
# the [-1] skips the first element; e.g. run c(1,2,3) then c(1,2,3)[-1]
heatmap_matrix <- as.matrix(heatmap_recast[-1])

# Use the days of the week as labels for the rows of heatmap_matrix
row.names(heatmap_matrix) <- as.vector(weekdays)

# Generate the heatmap of weekdays per hour
hchart(heatmap_matrix, type = "heatmap")

##
# Histogram analysis
##

# Add a posix.date column to the dataframe that stores the date in posixct format
gadata$posix.date <- as.POSIXct(gadata$date)

# Examine the distribution of sessions over time
ggplot(gadata, aes(x=posix.date, y=sessions)) + 
  geom_point() +
  scale_x_datetime(breaks=date_breaks('4 months'))

# Use some transparency and a trend line to find the general trajectory
ggplot(gadata, aes(x=posix.date, y=sessions)) +
  geom_point(alpha=0.1) +
  geom_smooth() +
  scale_x_datetime(breaks=date_breaks('4 months'))

# Repeat the same plot, but only show the month of November
november.rows <- subset(gadata, format(posix.date,'%m')=='11')

ggplot(november.rows, aes(x=posix.date, y=sessions)) + 
  geom_point() +
  scale_x_datetime(breaks=date_breaks('4 months'))

# Color each point in the scatterplot by the day on which that observation occured
ggplot(gadata, aes(x=posix.date, y=sessions, color=as.factor(weekday))) + 
  geom_point() +
  scale_x_datetime(breaks=date_breaks('4 months'))

# Compare Wednesday and Friday
plot <- ggplot(subset(gadata, weekday %in% c('Wednesday', 'Friday')),
    aes(x=posix.date, y=sessions, color=as.factor(weekday))) + 
  geom_point() +
  scale_x_datetime(breaks=date_breaks('6 months')) +
                                                # -- styling the chart --
  guides(color=guide_legend(title='')) +        # remove the legend title
  ggtitle('2016 Page Views') +                  # set a chart title
  xlab('Date') +                                # set an x axis label
  ylab('Total Sessions') +                      # set a y axis label
  theme(plot.title = element_text(hjust = 0.5)) # center the title

ggsave('page-views.png')

# Examine the number of days with each value of sessions
ggplot(gadata, aes(x=sessions)) +
  geom_bar(stat='bin', bins=30)
