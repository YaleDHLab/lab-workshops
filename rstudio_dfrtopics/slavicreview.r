#Create a new project in the folder that has the JSTOR data.

install.packages("devtools")
install_github("agoldst/dfrtopics")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("lubridate")
install.packages("stringr")
install.packages("rJava")
install.packages("mallet")



library(devtools)
options(java.parameters="-Xmx4g")
library(dfrtopics)
library(dplyr)
library(ggplot2)
library(lubridate)
library(stringr)
library(rJava)
library(mallet)


data_dir <- file.path("/Users/[YOUR USERNAME HERE]/Desktop/slavic")

# First we load metadata: 

metadata_file <- file.path(data_dir, "citations.tsv")
meta <- read_dfr_metadata(metadata_file)
# 
# "The word counts can be loaded into memory all at once with read_wordcounts, 
# which takes a vector of file names."
counts <- read_wordcounts(list.files(file.path(data_dir, "wordcounts"), full.names=T))


# "Here’s how we might tabulate how many words stoplisting will remove from each document:"
stoplist_file <- file.path("stoplist-russian.txt")
stoplist <- readLines(stoplist_file)
counts <- counts %>% wordcounts_remove_stopwords(stoplist)




# "Filter infrequent words. OCR’d text in particular is littered with hapax legomena.
# The long tail of one-off features means a lot of noise for the modeling process, 
# and you’ll likely want to get rid of these.
# For example, to eliminate all but roughly the 20,000 most frequent features:"
counts <- counts %>%
  wordcounts_remove_rare(20000)
  
  
  
  
  
# "MALLET cannot accept our counts data frame from R as is. 
# Instead, it wants a data frame with one row per document, 
# which it will then tokenize once again. This is silly, but easily handled:"
docs <- wordcounts_texts(counts)



# "To create the MALLET-ready input, which is called an InstanceList, we use:"
ilist <- make_instances(docs)



#
# "Now we launch the LDA algorithm"
#
# we ran 20, 50, 100, and 150, and agreed on 100
topic_model <- train_model(ilist, n_topics=50,
                 n_iters=300,
                 seed=1,
                 threads=4,
                 metadata=meta
)
#this can take quite a long time...
write_mallet_model(topic_model, "modeling_results")




summary(topic_model)
# create folder for topic browsing. note that folder name is 'browser-'+number of topics+formatted datetime
dfr_browser(topic_model, "slavic-review-browser", internalize=F)

# Type this in a terminal, not rStudio:
cd slavic-review-browser
bin/server


# to get a readout of the top N words by weight and first N topic labels, use these
# top_words(topic_model, n=10)
# topic_labels(topic_model, n=8)
