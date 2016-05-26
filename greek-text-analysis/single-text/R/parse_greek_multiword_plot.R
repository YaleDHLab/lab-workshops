# to install ggplot2
#install.packages("ggplot2")

library(ggplot2)

########################
# Single text analysis #
########################

greek <- scan("greek.xml", what="character", sep=" ")

# slice notation 
greek[10:20]

# join notation
greek.string <- paste(greek[10:20], collapse=" ")

# functional programming: length
length(greek)

# functional programming: lower
greek.lower <- tolower(greek)

# find index positions of word that's of interest
word.one.positions <- which(greek.lower == "εἰς")

# find index positions of any word in an array
word.two.positions <- which(greek.lower %in% c("τοῦ", "μετὰ"))

# check which words in the text are equal to εἰς
greek.lower[which(greek.lower=="εἰς")]

# for the above, we could also write
greek.lower[word.one.positions]

# create an x axis with one position for each word in the text of interest
text.time <- seq(1:length(greek.lower))

# initialize a vector with length = text length, and set all values to 0
text.vector <- rep(0, length(greek.lower))

# now change the text vector to indicate which words are of interest
text.vector[word.one.positions] <- "εἰς"
text.vector[word.two.positions] <- "τοῦ or μετὰ"

# convert text time into dataframe
dataframe <- as.data.frame(text.time)

# convert the integer sequence to class numeric
dataframe$text.time <- as.numeric(as.character(dataframe$text.time))

# add a column to df for boolean presence of word
dataframe$contains.word <- text.vector

# crossbar limits
limits <- aes(ymax=2, ymin=0)

# now we can plot the vector as a dispersion plot
plot <- ggplot(subset(dataframe, contains.word != 0), 
               aes(x=text.time, 
                   y=as.factor(contains.word != 0), 
                   color=as.factor(contains.word))) +
  geom_linerange(limits) +  # draw lines where the words are present
  scale_y_discrete() +      # ensure y axis is treated as a discrete distribution
  xlab("Word number") +     # provide x axis label
  ylab("") +                # provide y axis label
  theme(
    axis.text.y=element_blank(),          # remove the axis text from the y axis
    axis.ticks.y=element_blank(),         # remove ticks from the y axis 
    plot.margin = unit(c(1,1,1,1), "cm")  # create margin around plot
  ) +
  labs(color="Word") +                                            # provide title for legend
  ggtitle("Distribution of selected words in Barnabae Epistula")  # provide title for plot


# save the plot to disk
ggsave(filename="multiple_greek_words_plot.png")
