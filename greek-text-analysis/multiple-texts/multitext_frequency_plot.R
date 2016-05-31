# uncomment to install the ggplot2 package
# install.packages("ggplot2")
# uncomment to install the XML package
# install.packages("XML")

library(ggplot2)
library(XML)

###############################
# Warming up with XML parsing #
###############################

# find all texts in the working directory
# `intern` flag means to stuff the results into an internal variable
all_files <- system("ls", intern=TRUE)

# parse the hierarchical tree structure in the first document
file_one_tree <- htmlTreeParse(all_files[1], useInternalNodes = TRUE)

# extract the content of each speaker tag in the text 
file_one_speakers <- xpathSApply(file_one_tree, "//speaker", xmlValue)

# suppose we want to know the total number of times each speaker speaks
file_one_speaker_table <- table(file_one_speakers)

# convert to dataframe
speakers.df <- as.data.frame(file_one_speaker_table)

# rename columns
# pass colnames function the data frame and the new names
colnames(speakers.df) <- c("speaker", "frequency")

# convert frequency column to a numeric type
speakers.df$frequency <- as.numeric(as.character(speakers.df$frequency))

# plot the distribution of speakers
# give ggplot the dataframe, the "aesthetics", and 
#      info on how to distinguish visually the bars in the graph
# x axis is a reordered list of speakers in frequency descending
ggplot(speakers.df, aes(x=reorder(speaker, -frequency), y=frequency, fill=reorder(speaker, -frequency))) +
  geom_bar(stat="identity")
# remove fill arg to get monochrome
# ggplot(speakers.df, aes(x=reorder(speaker, -frequency), y=frequency))
#   geom_bar(stat="identity")


###################################
# Getting started with loops in R #
###################################

# loop over those texts, and print each
# just for demonstration purposes; no residual use of this in following code
for (file in all_files) {
  print(file)
}

# initialize empty dataframe
all_speakers.df <- data.frame(file_speakers=character(), Freq=numeric(), file=character())

for (file in all_files) {
  file_tree <- htmlTreeParse(file,  useInternalNodes = TRUE)
  file_speakers <- xpathSApply(file_tree, "//speaker", xmlValue)
  speaker_table <- table(file_speakers)
  file_speakers.df <- as.data.frame(speaker_table)
  file_speakers.df$file <- file
  all_speakers.df <- rbind(file_speakers.df, all_speakers.df)
}

# rename the columns in the dataframe
colnames(all_speakers.df) <- c("speaker", "frequency", "play")

# plot the distribution of speakers within each play
# the reorder() arguments simply reorder the bars and the colors
# to ensure that the first bar for each text represents
# the most present character for that text
# plot the distribution of speakers within each play
ggplot(all_speakers.df, aes(x=reorder(speaker, -frequency), y=frequency)) +
  
  # use a bar chart
  geom_bar(stat="identity") +
  
  # free_x allows one to only show frequency bars for 
  # the characters that actually appear in a text 
  facet_wrap(~play, scales="free_x") + 
  
  # remove the legend from the plot
  theme(legend.position="none") # remove legend


#########################################
# Extracting attributes from many files #
#########################################

# initialize an empty dataframe
all_text_data.df <- data.frame(word_number=numeric(), contains_word=character(), file=character())

# loop over each file and extract the data of interest
for (file in all_files) {

  ######################
  # extract plain text #
  ######################
    
  # extract the XML tree
  file_tree <- htmlTreeParse(file, useInternalNodes = TRUE)
  
  # select all of the speaker nodes
  speaker_nodes <- getNodeSet(file_tree, "//speaker")
  
  # remove the speaker nodes from file_tree
  # modifies file in place
  removeNodes(speaker_nodes)
  
  # also remove the teiHeader nodes
  removeNodes(getNodeSet(file_tree, "//teiHeader"))
  
  # get text between <text> tags
  file_text <- xpathSApply(file_tree, "//text", xmlValue)
  
  # TEXT CLEANING
  # replace \n . , and ; with whitespace
  file_text_clean <- gsub("\n", " ", file_text)
  file_text_clean <- gsub("\\.", " ", file_text_clean)
  file_text_clean <- gsub(",", " ", file_text_clean)
  file_text_clean <- gsub(";", " ", file_text_clean)
  
  # tokenize the text on one or more whitespaces
  split_text <- unlist(strsplit(file_text_clean, "\\s+"))
  
  # find all instances of one or more words from one group of words
  group_one_positions <- which(split_text %in% c("τοῦ", "μετὰ"))
  
  # find all instances of one or more words from another group of words
  group_two_positions <- which(split_text %in% c("οἵ", "δʼ"))
  
  # create an x axis with one position for each word in the text of interest
  word_number <- seq(1:length(split_text))
  
  # initialize a vector with length = text length, and set all values to 0
  text_vector <- rep(0, length(split_text))
  
  # change the text vector to indicate which words are of interest
  text_vector[group_one_positions] <- "τοῦ or μετὰ"
  text_vector[group_two_positions] <- "οἵ or δʼ"
  
  # convert this text's text_vector to a dataframe
  text_data.df <- as.data.frame(word_number)
  
  # convert the integer sequence to class numeric
  text_data.df$word_number <- as.numeric(as.character(text_data.df$word_number))
  
  # add a column to df for boolean presence of word
  text_data.df$contains_word <- text_vector
  
  # store the current text title in the dataframe
  text_data.df$title <- file
  
  # append the current df to the master df
  all_text_data.df <- rbind(text_data.df, all_text_data.df)
}

###############
# create plot #
###############

# crossbar limits
limits <- aes(ymax=2, ymin=0)

# now we can plot the vector as a dispersion plot
plot <- ggplot(subset(all_text_data.df, contains_word != 0), 
               aes(x=word_number, 
                   y=as.factor(contains_word != 0), 
                   color=as.factor(contains_word))) +
  geom_linerange(limits) +  # draw lines where the words are present
  scale_y_discrete() +      # ensure y axis is treated as a discrete distribution
  xlab("Word number") +     # provide x axis label
  ylab("") +                # provide y axis label
  theme(
    axis.text.y=element_blank(),          # remove the axis text from the y axis
    axis.ticks.y=element_blank(),         # remove ticks from the y axis 
    plot.margin = unit(c(1,1,1,1), "cm")  # create margin around plot
  ) +
  labs(color="Word") +                                        # provide title for legend
  ggtitle("Distribution of selected words in Greek texts") +  # provide title for plot
  facet_wrap(~title, scale="free_x") 
  # remove the scale arg for each plot to normalize to the same word count as longest file
  # facet_wrap(~title) 


# to save the plot to disk, pipe the output of the
# function call above to an object called plot, then call:
ggsave(filename="multiple_greek_words_multiple_texts_plot.png")
