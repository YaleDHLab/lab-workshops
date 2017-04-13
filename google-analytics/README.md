# Google Analytics with R

Google Analytics is a fantastic resource for analyzing patterns in website traffic. Using the `googleAnalyticsR` package, one can now process Google Analytics in R very quickly. This workshop gives a brief introduction to this library, with the hope of preparing users for more advanced work with Google Analytics.

## Getting Started with R

To get started with R, you'll need to [install R](https://cran.cnr.berkeley.edu/) on your machine. Once that's all done, you will also want to [install RStudio](https://www.rstudio.com/products/rstudio/download/), the standard "Integrated Development Environment" (text-editor + helpful addons) for R programming.

## Getting Started with Google Analytics

To get started with Google Analytics, you'll need to [install Google Analytics](https://support.google.com/analytics/answer/1008080?hl=en) on a website you oversee.

Once Google Analytics is installed, you'll need to identify the "View Id" for your given domain. You can obtain this by visiting the [Google Analytics Query Explorer](https://ga-dev-tools.appspot.com/query-explorer/). The "View" dropdown will contain a list of all domains on which you've installed Google Analytics. Select an option from that dropdown and note the value within the `ids` field. The value after the `ga:` prefix is the View Id you need to use for what follows:

![Google Analytics view id](https://github.com/YaleDHLab/lab-workshops/raw/master/google-analytics/images/google-analytics-view-id.png)

Once you have a view id, you're ready to process some data!

### Processing Google Analytics Data with R

Once the requirements above are settled, you're ready to process Google Analytics data with R. The first step is to install the package we'll use for this session, [googleAnalyticsR](http://code.markedmondson.me/googleAnalyticsR/). This package will manage all of the integration between R and Google Analytics, and has some nice helper functions for querying the Google Analytics API.

### Load Dependencies

Like all R packages, the googleAnalyticsR package must be loaded into a script in order to be used. The following lines will check to see if googleAnalyticsR is already installed on your machine, and if not, will install the package:

```
##
# Load dependencies
##

# Install the google analytics package if it isn't installed
if(!require(googleAnalyticsR)) install.packages("googleAnalyticsR")

# Load the googleAnalyticsR library
library(googleAnalyticsR)
```

### Authenticate with Google Analytics

Once this package is loaded, we're ready to authenticate with Google with the following line:

```
##
# Authenticate with Google
##

# Grant the application access to your analytics data
ga_auth()
```

Running this line will spring a browser window that will ask you to verify whether you wish to give googleAnalyticsR access to your Google Analytics data.

If you agree and close the window, you'll see a new `.httr-oauth` in your current directory. If you're on a unix OS, you can see this file by submitting an `ls` command to your system through R:

```
# To see the token, submit an 'ls' call to the operating system
system('ls -lsah')
```

This token grants individuals access to your Google Analytics data, so protect this file!

### Query Google Analytics for Data

Once the application has access to your Google Analytics data, you're ready to query the GA API. To do so, we'll need to use the view id you obtained above:

```
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
```

These lines use the `google_analytics_4()` function to make a query to the GA API. To learn more about this function, you can use one of R's inbuilt queries for documentation:

```
# To review the documentation on the function we just ran:
?google_analytics_4

# An alternative way to get documentation
help(google_analytics_4)

# You can also search available documentation
help.search('Google Analytics')
```

### Groking the gadata object

When using inbuilt functions like `google_analytics_4` it's nice to examine the returned object. One way to do so is to use the `head(gadata)` function, which will show the first few lines from the gadata object:

```
> head(gadata)
        date hour sessions
1 2017-02-12   00        0
2 2017-02-12   01        0
3 2017-02-12   02        0
4 2017-02-12   03        0
5 2017-02-12   04        0
6 2017-02-12   05        0
```

The output included above indicates that `gadata` contains rows named 'date', 'hour', and 'sessions'.

To check the total number of rows in gadata, we could use `nrow()`:

```
> nrow(gadata)
[1] 1464
```

If we wanted to check the class of `gadata`, we could use `class()`:

```
> class(gadata)
[1] "data.frame"
```

The output included above indicates that gadata is an object of class 'data.frame'. 

### Creating Sample gadata

If you don't have a Google Analytics account setup, or you don't want to process your real data just yet, you can use the following lines to generate some artificial data with the same structure as the `gadata` object described above:

```
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
```

### Generating a heatmap of pageviews

With the gadata object in hand, one can prepare a variety of plots to study trends in user behavior. One chart that can be useful to study is a heatmap of pageviews per hour per day over a range of time. To do so, let's load some dependencies:

```
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
```

In case it's not present there already, let's add a column to the gadata object that indicates the day of the week on which each day occurred:

```
# Get a list of the days of the week in order
weekdays <- c('Monday', 'Tuesday', 'Wednesday', 'Thursday',
              'Friday', 'Saturday', 'Sunday')

# Add a day of the week to each observation in the dataframe
gadata$weekday <- ordered(weekdays(gadata$date), levels=weekdays)
```

Then let's create a new object that contains  only the weekday, hour,
and sessions columns:

```
# Create a subset of the gadata object that contains only the
# weekday, hour, and sessions columns
heatmap_data <- select(gadata, weekday, hour, sessions)
```

Next we'll use the `aggregate()` function to find the sum of all sessions for each combination of weekday and hour:

```
# Use the sum function to aggregate the total number of sessions
# for each weekday+hour combination in heatmap_data
heatmap_sums <- aggregate( sessions ~ 
                 weekday + hour,
                 sum,
                 data=heatmap_data)
```

If we run `View(heatmap_sums)` we can see that the object we just made has columns for weekday, hour, and sessions. The plot function we're going to call requires us to provide data in a distance matrix type structure, where each column is an hour of the day, each row is a day of the week, and each cell value is the sum of sessions for that hour of that day. To push our data into this format, we can run:

```
# Push the data into the format required by highcharts ->
# each column will be an hour and each row a day of the week
heatmap_recast <- spread(heatmap_sums, hour, sessions)
```

We now need to remove the first column from `heatmap_recast`, as this column contains the days of the week as strings:

```
# Make this "data frame" into a "matrix";
# the [-1] skips the first element; e.g. run c(1,2,3) then c(1,2,3)[-1]
heatmap_matrix <- as.matrix(heatmap_recast[-1])
```

Finally, let's produce a heatmap:

```
# Use the days of the week as labels for the rows of heatmap_matrix
row.names(heatmap_matrix) <- as.vector(weekdays)

# Generate the heatmap of weekdays per hour
hchart(heatmap_matrix, type = "heatmap")
```

This returns a chart that looks like this:

![Views Heatmap](https://github.com/YaleDHLab/lab-workshops/raw/master/google-analytics/plots/views-heatmap.png)

Congratulations--you've produced a heatmap of pageviews with R!

## Charting with ggplot2

One can also use the popular ggplot2 library to produce a variety of charts with the gadata object. The following plot, for instance, will compare page views on Wednesdays and Fridays over time:

```
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

plot
```

![Page views on Wednesdays and Friday](https://github.com/YaleDHLab/lab-workshops/raw/master/google-analytics/plots/page-views.png)

## Going Further

There are a number of great resources on the `googleAnalyticsR` package. The main page for the package lists the following resources:

* Dartistics.com is a website dedicated to using R with digital analytics, and has a page on [getting up and running](http://www.dartistics.com/api-google-analytics.html) with googleAnalyticsR
* Michal Brys has an [online book](https://michalbrys.gitbooks.io/r-google-analytics/content/chapter6/device-comparsion.html) on using Google Analytics with R that uses googleAnalyticsR
* Ryan Prazki has created a [video tutorial](http://www.ryanpraski.com/google-analytics-r-tutorial/) on how to get up and running quickly: Google Analytics R Video Tutorial
* Ryan also has a tutorial on using googleAnalyticsR to do [scroll tracking analysis](http://www.ryanpraski.com/scroll-depth-tracking-analysis-with-google-analytics-r) in a heatmap
* Jules has a nice post on using a [Markov model to create an attribution model](http://stuifbergen.com/2016/11/conversion-attribution-markov-model-r/) with googleAnalyticsR data
* Tim Wilson has a guide on getting up and running with [R for digital analysts](http://analyticsdemystified.com/google-analytics/tutorial_pulling_google_analytics_data_with_r/)
* Guide to using googleAnalyticsR in [Japanese](https://www.karada-good.net/analyticsr/r-520) and here
* Alenlytics has a guide that also includes using the RStudio Addin for [authentication](http://alenlytics.com/connecting-r-with-google-analytics/)
* Mario Martinez has a guide on using googleAnalyticsR in [Spanish](http://www.doctormetrics.com/2017/01/03/nueva-version-de-la-api-de-google-analytics-r-statistics/#.WLVOWhAvpBI)
* Vincent has a tutorial on using Twitters AnomalyDetection package with googleAnalyticsR in [French](https://data-seo.fr/2016/05/02/detecter-vos-marronniers-avec-r/)
