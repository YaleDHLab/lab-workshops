from __future__ import division
from scipy.cluster.hierarchy import dendrogram, linkage
from collections import defaultdict, Counter
from sklearn.manifold import TSNE
from os.path import basename
import matplotlib.pyplot as plt
from umap import UMAP
import numpy as np
import csv, json

np.set_printoptions(suppress=True)

def plot_labelled_points(points, labels):
  '''
  Create a 2d scatterplot from points with labels
  @args:
    [arr] points: contains one member with ordered x,y,z vals for each point
    [str] labels: contains one string label for each member of `points`
  @returns:
    None
  '''
  fig, ax = plt.subplots(figsize=(16,10))

  # add each point and label to the plot
  for idx, _ in enumerate(points):
    x, y = points[idx]
    label = labels[idx]
    ax.scatter(x, y, s=0.5, color='b')
    ax.text(x, y, label, size=9, color='k')
  return plt

def project_terms(method='umap'):
  '''
  Return a model that can project points into 2D
  @args:
    {str} method: the dimension reduction method to use
  @returns:
    a model that supports a `.fit_transform()` method
  '''
  if method == 'tsne':
    return TSNE(n_components=2, random_state=0)
  elif method == 'umap':
    return UMAP(n_neighbors=5, min_dist=2, spread=2)
  else:
    raise Exception('The requested model type could not be found!')

def plot_term_scatterplot(model, threshold=0.1, method='umap'):
  '''
  Project the term vectors down into a 2D space and visualize
  @args:
    nmf.nmf.NMF model: a nmf model
    float threshold: the minimum concentration a term must have in
      one or more topics to be visualized (increasing will limit the
      displayed terms to more topic-focused terms)
    string method: the method used to project term vectors down
      into 2D {'tsne', 'umap'}
  @returns:
    void
  '''

  # topics_by_terms.T has shape (n_terms, n_topics). Find the terms in that matrix
  # that have 0.1 or greater concentration in a given topic
  concentrated = np.amax(model.topics_by_terms.T, axis=1) >= threshold
  indices = [c for c, i in enumerate(concentrated) if i == True]

  # get the labels for the selected terms
  labels = [model.feature_names[i] for i in indices]

  # get the selected term vectors
  term_vectors = model.topics_by_terms.T[indices]

  # build a UMAP or TSNE model of the selected terms
  projection_model = project_terms(method=method)

  # fit the model
  fit_model = projection_model.fit_transform( term_vectors )

  # draw the term scatterplot
  plot_labelled_points(fit_model, labels)

def read_csv_metadata(*args, **kwargs):
  '''
  @args:
    str csv_filepath: the path to a CSV metadata file with
      columns in the following order:
        filename, title, year, author
  @kwargs:
    str quote: the character used for quoting in the csv
    str delimiter: the character used for delimiting fields in the csv
    str newline: the character used for newlines in the csv
  @returns:
    dict: d[filename] = {'title': '', 'year': '', 'author': ''}
  '''
  csv_filepath = args[0]
  quote = kwargs.get('quote', '"')
  delimiter = kwargs.get('delimiter', ',')
  newline = kwargs.get('newline', '\n')
  # parse the csv into the dict structure
  d = {}
  with open(csv_filepath, newline=newline) as f:
    reader = csv.reader(f, delimiter=delimiter, quotechar=quote)
    for row in reader:
      filename, title, year, author = row
      d[filename] = {
        'title': title,
        'year': year,
        'author': author,
      }
  return d

def plot_document_similarity(model, csv, **kwargs):
  '''
  Plot the similarity between documents in an NMF model
  @args:
    nmf.nmf.NMF model: a nmf model
    str csv: the path to a CSV metadata file
  @kwargs:
    int n_docs: the number of documents to include in the plot
    int fig_width: the width of the generated figure
    int fig_height: the height of the generated figure
  @returns:
    void
  '''

  # pull out kwargs
  n_docs = kwargs.get('n_docs', 100)
  fig_width = kwargs.get('fig_width', 60)
  fig_height = kwargs.get('fig_height', 10)

  # parse out metadata
  metadata = read_csv_metadata(csv)
  filenames = [basename(i) for i in model.infiles]
  labels = [metadata[i]['title'] for i in filenames]

  # ensure there is one label for each element in model.infiles
  if len(model.infiles) != len(labels):
    print('Please provide one label for each document in model.infiles.')
    print('You provided', len(labels), 'labels and model.infiles contains',
      len(model.infiles), 'entries.')
    return

  labels = labels[:n_docs]
  plt.figure(figsize=(fig_width, fig_height))
  plt.title('Hierarchical Document Similarity')
  plt.ylabel('distance')

  # visualize the first 100 documents
  X = model.documents_by_topics[:n_docs]
  X = np.nan_to_num(X)
  Z = linkage(X, 'ward')

  # leaf_rotation rotates the x axis label
  dendrogram(Z, leaf_rotation=90.0, leaf_font_size=14.0, labels=labels)
  plt.show()

def plot_topics_over_time(model, csv, **kwargs):
  '''
  Plot the distribution of each topic over time
  @args:
    nmf.nmf.NMF model: a nmf model
    str csv: the path to a CSV metadata file
  @kwargs:
    int fig_height: height of the figure
    int fig_width: width of the figure
  @returns:
    void
  '''
  metadata = read_csv_metadata(csv)
  fig_height = kwargs.get('fig_height', 30)
  fig_width = kwargs.get('fig_width', 10)

  # use a defaultdict to store the presence of each topic over time
  # structure: d[topic][year] = [freq, freq, freq]
  topic_year_freqs = defaultdict(lambda: defaultdict(list))

  # pluck out the filename
  for i in model.docs_to_topics:
    filename = basename(i)
    year = int(metadata[filename]['year'])
    for topic_idx in model.docs_to_topics[i]:
      topic_freq = model.docs_to_topics[i][topic_idx]
      topic_year_freqs[topic_idx][year].append(topic_freq)

  # find the mean presence of each topic in each year
  for topic in topic_year_freqs:
    for year in topic_year_freqs[topic]:
      n_observations = len(topic_year_freqs[topic][year])
      freq_sum = sum(topic_year_freqs[topic][year])
      topic_year_freqs[topic][year] = freq_sum / n_observations

  # create one subplot for each topic
  f, axes = plt.subplots(len(topic_year_freqs.keys()), 1)
  f.set_figheight(fig_height)
  f.set_figwidth(fig_width)
  for c, i in enumerate(topic_year_freqs):
    years = sorted(topic_year_freqs[i].keys())
    vals = [topic_year_freqs[i][year] for year in years]
    label = ' '.join(model.topics_to_words[i])
    axes[c].stackplot(years, vals)
    axes[c].set_title(label)
  plt.tight_layout()