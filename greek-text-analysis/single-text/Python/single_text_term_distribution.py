#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required packages
import nltk, codecs
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go

# specify plotly api credentials
py.sign_in('YOUR_PLOTLY_USERNAME', 'YOUR_PLOTLY_API_KEY')

# make an empty list. Each member of this list will be a 0,1
# to indicate whether the given word in the text is a word of interest
words_in_text = []

# populate a list of words that are of interest
words_of_interest = [u"τὸ", u"ὦ"]

# read the text into memory and split it into a list of words
with codecs.open("greek.xml", 'r', 'utf-8') as f:
  f = f.read()
  words = f.split()

  for w in words:
    
    # here we can write one of two options
    # if w == u"\u1f00\u03bd\u03b1\u03c0\u03bb\u03b7\u03c1\u03bf\u1fe6\u03c4\u03b5":
    #   or
    # if w == u"ἀναπληροῦτε" 
   
    # if the word is of interest, indicate that fact by adding
    # 1 to the words_in_text list, else add a 0 to the list
    if w in words_of_interest:
      words_in_text.append(1)
    else:
      words_in_text.append(0)

# plot the results
n_observations = len(words_in_text)
x_axis_vals = range(n_observations)
width = 1/1.5
plt.bar(x_axis_vals, words_in_text, width, color="blue") 
     
# call the plotting service to show the results
fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='time_series')
