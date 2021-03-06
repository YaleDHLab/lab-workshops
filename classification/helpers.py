from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
from collections import defaultdict
import matplotlib.style as style
import matplotlib.pyplot as plt
import numpy as np
import scattertext
import warnings
import seaborn
import pandas
import spacy

# quiet scipy future warnings
warnings.filterwarnings('ignore')

# decision boundary grid colors
grid_colors = ListedColormap([
  '#ff8585',
  '#6db4f3',
])

# decision boundary point colors
point_colors = ListedColormap([
  '#ff0000',
  '#0000ff',
])

def plot_decision_boundary(clf, X, labels, margin=0.4, mesh_unit=0.2, proba=False):
  '''
  Plot the classification decision for each point in a quantized grid
  From: http://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html

  @args:
    {class} clf: a class that has a method .predict() that takes as input
      an array of k dimensional values and returns an array with shape n,1
      where n = the number of observations in the input array. This returned
      array of values should contain class predictions--one per input element.
      nb: if proba=True, the class should contain a method `.decision_function()`
      that should return an array with shape n,1 that contains probability
      values for a given class prediction. See scikit classifiers for examples
      of both methods.

  @returns:
    void
  '''
  style.use('seaborn-white')
  # convert the input matrix to an array if necessary
  if isinstance(X, list):
    X = np.array(X)
  elif isinstance(X, pandas.core.series.Series) or isinstance(X, pandas.core.frame.DataFrame):
    X = X.to_numpy()
  # convert the labels to an array if necessary
  if isinstance(labels, pandas.core.series.Series):
    labels = labels.to_numpy()
  # convert the labels to integers if they're not integers
  labels_integerized = False
  if isinstance(labels[0], str):
    d = defaultdict(lambda: len(d))
    labels = [d[i] for i in labels]
    labels_integerized = True
  # find the min value in the first column and subtract `margin`
  x_min = X[:, 0].min() - margin
  # find the max value in the first column and add `margin`
  x_max = X[:, 0].max() + margin
  # find the minimum value in the second column and subtract `margin`
  y_min = X[:, 1].min() - margin
  # find the minimum value in the second column and add `margin`
  y_max = X[:, 1].max() + margin
  # get a list of values from min to max, counting by `mesh_unit`
  x_range = np.arange(x_min, x_max, mesh_unit)
  y_range = np.arange(y_min, y_max, mesh_unit)
  # create a dense grid with one row for each value in x_range and
  # one column for each value in y_range
  xx, yy = np.meshgrid(x_range, y_range)
  # `np.ravel` flattens a multidimensional array to a single dimension.
  # `np.c_` makes its first and second args the first and second columns in a 2D
  # array, so np.c_[xx.ravel(), yy.ravel()] has one 2D observation per grid unit
  grid_vals = np.c_[xx.ravel(), yy.ravel()]
  # plot continuous predictions if proba == True, else discrete classifications
  if proba:
    # some classifiers use decision_function to return continuous probabilities
    # while others use predict_proba
    if hasattr(clf, 'decision_function'):
      Z = clf.decision_function(grid_vals)
    else:
      Z = clf.predict_proba(grid_vals)[:,1]
  else:
    Z = clf.predict(grid_vals)
  # interize the predictions if necessary
  if labels_integerized: Z = np.array([d[i] for i in Z])
  # reshape Z (a 1D array of classification decisions) to a 2D x by y grid
  Z = Z.reshape(xx.shape)
  # plot the background decision boundary
  cmap = plt.cm.RdBu if proba else grid_colors
  plt.contourf(xx, yy, Z, cmap=cmap, alpha=0.8)
  # plot the observations
  plt.scatter(X[:,0], X[:,1], s=30, c=labels, cmap=point_colors, edgecolors='#000000')


def plot_distance(arr):
  '''
  Given `arr` with two arrays, each of two or three elements,
  plot the points at positions `arr[0]` and `arr[1]`
  and plot lines between those two points

  @args:
    arr [arr]: an array composed of 2d or 3d arrays
  @returns:
    void
  '''
  if len(arr[0]) == 2:
    plot_distance_2d(arr)
  elif len(arr[0]) == 3:
    plot_distance_3d(arr)


def plot_distance_2d(arr):
  '''
  Given `arr` with two 2-element arrays, plot the points
  at positions `arr[0]` and `arr[1]` and plot lines between
  those two points

  @args:
    arr [arr]: an array composed of 2d arrays
  @returns:
    void
  '''
  a, b = arr
  df = np.array([a, b])

  # point data: pattern for drawing points is:
  # ax.scatter(x_vals, y_vals, z_vals)
  plt.scatter(df[:,0], df[:,1], s=100, c=['blue', 'orange'], alpha=1.0, edgecolors='#000000')

  # add point labels
  plt.text(0.05, 0.05, 'a', fontsize=20, horizontalalignment='center')
  plt.text(0.95, 0.95, 'b', fontsize=20, horizontalalignment='center')

  # line data: pattern for drawing lines is:
  # ax.plot([x_start, x_end], [y_start, y_end], zs=[z_start, z_end])
  plt.plot( [a[0], b[0]], [a[1], a[1]], c='red' )    # x-line
  plt.plot( [b[0], b[0]], [a[1], b[1]], c='purple' ) # y-line
  plt.plot( [a[0], b[0]], [a[1], b[1]], c='gray', linestyle=':' )  # direct line

  # add axis labels
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.show()


def plot_distance_3d(arr):
  '''
  Given `arr` with two 3-element arrays, plot the points
  at positions `arr[0]` and `arr[1]` and plot lines between
  those two points.

  @args:
    arr [arr]: an array composed of 3d arrays
  @returns:
    void
  '''
  a, b = arr
  df = np.array([a, b])

  fig = plt.figure()
  ax = fig.gca(projection='3d')

  # point data: pattern for drawing points is:
  # ax.scatter(x_vals, y_vals, z_vals)
  ax.scatter(df[:,0], df[:,1], df[:,2], s=100, c=['blue', 'orange'], alpha=1.0)

  # label points
  ax.text(0.1, 0.1, 0, 'a', fontsize=20, horizontalalignment='center')
  ax.text(0.9, 0.9, 1.0, 'b', fontsize=20, horizontalalignment='center')

  # line data: pattern for drawing lines is:
  # ax.plot([x_start, x_end], [y_start, y_end], zs=[z_start, z_end])
  ax.plot( [a[0], b[0]], [a[0], a[0]], zs=[a[0], a[0]], c='red' )  # x-line
  ax.plot( [b[0], b[0]], [a[0], b[0]], zs=[a[0], a[0]], c='purple' ) # y-line
  ax.plot( [b[0], b[0]], [b[0], b[0]], zs=[a[0], b[0]], c='green' )  # z-line
  ax.plot( [a[0], b[0]], [a[0], b[0]], zs=[a[0], b[0]], c='gray', linestyle=':' )  # direct line

  # add axis labels
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  plt.show()


def plot_iforest_decision_boundary(*args, **kwargs):
  '''
  Create and display the decision boundary for an isolation forest.
  '''
  clf = args[0] # the isolation forest classifier
  X = args[1]   # the input array of observations used to train the classifier
  new_vals = args[2] # the array of observations classified by the classifier
  result = args[3]   # the classification results from the classifier
  margin = kwargs.get('margin', 6)   # margin around the plot
  mesh   = kwargs.get('grid_x', 0.5) # the size of each colormesh grid unit
  x_lims = kwargs.get('x_lims', (-13, 12)) # the min max x values to display
  y_lims = kwargs.get('y_lims', (-13, 5)) # the min max y values to display
  # get the x and y grid domains
  x_domain = [ X[:, 0].min() - margin, X[:, 0].max() + margin ]
  y_domain = [ X[:, 1].min() - margin, X[:, 1].max() + margin ]
  # get a list of values from min to max, counting by `mesh`
  x_range = np.arange(x_domain[0], x_domain[1], mesh)
  y_range = np.arange(y_domain[0], y_domain[1], mesh)
  # create the data with which to color the background grid
  xx, yy = np.meshgrid(x_range, y_range)
  # classify each unit of the grid
  Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
  # reshape Z into a 2D grid
  Z = Z.reshape(xx.shape)
  # fill in the grid values
  plt.contourf(xx, yy, Z, cmap=plt.cm.YlGn)
  # add the training points; edgecolors='k' is short for 'edgecolors'='black'
  train_p = plt.scatter(X[:,0], X[:,1], c='green', edgecolors='k', alpha=0.4)
  # separate new_vals into outliers and "inliers" based on result
  outliers = []
  inliers = []
  for idx, i in enumerate(result):
    if result[idx] == 1:
      inliers.append(new_vals[idx])
    else:
      outliers.append(new_vals[idx])
  outliers = np.array(outliers)
  inliers = np.array(inliers)
  # plot the inliers and outliers
  in_p = plt.scatter(inliers[:,0], inliers[:,1], c='white', edgecolors='k')
  out_p = plt.scatter(outliers[:,0], outliers[:,1], c='red', edgecolors='k')
  # limit the axis ranges
  plt.xlim(x_lims)
  plt.ylim(y_lims)
  # add a title to the plot
  plt.title('Isolation Forests Decision Boundary')
  # add a legend to the plot
  plt.legend([train_p, in_p, out_p], [
    'training observation',
    'classified as non-outlier',
    'classified as outlier',
  ], loc=[0.025, 0.05], framealpha=0.97)
  plt.show()


def plot_distinctive_words(x_label='', x_files=[], y_label='', y_files=[], max_words=10000, max_files=100):
  '''
  Create a scatterplot that shows the distinctive words among x_files and y_files.
  Use x_label as the x axis label and y_label as the y_axis label.
  Return HTML content that can be rendered to show the distinctive words.
  '''
  rows = []
  for i in x_files[:max_files]: rows.append([ x_label, ' '.join(open(i).read().split()[:max_words]) ])
  for i in y_files[:max_files]: rows.append([ y_label, ' '.join(open(i).read().split()[:max_words]) ])
  df = pandas.DataFrame(rows, columns=['Group', 'Text'])
  nlp = spacy.load('en')
  nlp.max_length = 2**64
  corpus = scattertext.CorpusFromPandas(
    df,
    category_col='Group',
    text_col='Text',
    nlp=nlp).build()
  html = scattertext.produce_scattertext_html(corpus,
    category=y_label,
    category_name=y_label,
    not_category_name=x_label,
    minimum_term_frequency=5,
    width_in_pixels=1000)
  return html


def plot_word_counts(files=[], x_word='', y_word=''):
  '''Given a list of file paths and word/s for the x/y axes, create a plot of the word counts'''
  style.use('fivethirtyeight')
  # check that the user provided files to process
  if not files: raise Exception('Please provide a list of files to the `files` argument')
  # check that the user provided one or more words to plot
  if not x_word and not y_word: raise Exception('Please provide an `x_word` and/or `y_word` argument')
  # accumulate the data for the pandas dataframe
  rows = []
  for i in files:
    if   'archeological' in i: group = 'archeological'
    elif 'medical' in i: group = 'medical'
    elif 'geometrical' in i: group = 'geometrical'
    elif 'astronomical' in i: group = 'astronomical'
    else: raise Exception('''
      Rutroh! We only expected to use this function to plot two simple scatterplots in our workshop.
      If you are interested in plotting word counts in other datasets, please consult this blog post:
      https://amiradata.com/how-to-draw-a-scatter-plot-python/
    ''')
    colors = {
        'archeological': 'blue',
        'medical': 'red',
        'geometrical': 'orange',
        'astronomical': 'purple',
    }
    with open(i) as f:
      text = f.read()
      rows.append([
        text.count(x_word) if x_word else 0,
        text.count(y_word) if y_word else 0,
        group,
        colors[group],
      ])
  x_col = 'Count_{}'.format(x_word)
  y_col = 'Count_{}'.format(y_word)
  df = pandas.DataFrame(rows, columns=[x_col, y_col, 'Group', 'Color'])
  # determine which variables to use on the axes
  x_var = x_col if x_word else 'Group'
  y_var = y_col if y_word else 'Group'
  fig, ax = plt.subplots(figsize=(10, 6))
  seaborn.scatterplot(data=df, hue='Group', x=x_var, y=y_var, s=100, alpha=0.6)
  if x_word: ax.set_xlabel('Count of word "{}" per document'.format(x_word))
  if y_word: ax.set_ylabel('Count of word "{}" per document'.format(y_word))
  plt.legend(loc=1)
  # get the title
  title_middle = ''
  if x_word and y_word: title_middle += '"{}" and "{}"'.format(x_word, y_word)
  elif x_word: title_middle += '"{}"'.format(x_word)
  elif y_word: title_middle += '"{}"'.format(y_word)
  title = 'Counts of {} per document'.format(title_middle)
  plt.title(title)