import os
# remove tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.applications import inception_v3, InceptionV3, imagenet_utils
from keras.preprocessing.image import load_img, img_to_array
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
from github import Github
import numpy as np
import os, uuid


# initialize inception model
model = InceptionV3(weights='imagenet')


def get_inception_vector(image_path):
  '''
  @arg image_path str: the path to an image
  @returns numpy.ndarray: an array containing the inception model weights for the input image
  '''
  # VGG16, VGG19, and ResNet take 224×224 images; InceptionV3 and Xception take 299×299 inputs
  img = load_img(image_path, target_size=(299,299))

  # convert the image to an array
  arr = img_to_array(img)

  # scale the array to fit the model
  arr = inception_v3.preprocess_input(arr)

  # complete forward pass through model
  return model.predict(np.array([arr])).squeeze()


def get_inception_vector_labels(image_vector):
  '''
  @arg image_vector numpy.ndarray: the inception image vector for an image
  @returns [(imagenet_id, label, probability)]: a list of tuples with the form:
    (imagenet_id, label, probability)
  '''
  # check if the input image vector is a 1D array
  if len(image_vector.shape) > 1:

    # raise an exception
    raise Exception('The input to get_inception_vector_labels should be a single image vector with shape (n,)')

  # return the label prediction
  return imagenet_utils.decode_predictions(np.expand_dims(image_vector, 0))[0]


def display_image(image_path):
  '''
  @arg image_path str: the path to an image
  @returns matplotlib.pyplot: a plot of the input image
  '''
  plt.imshow(img_to_array(load_img(image_path)) / 255)
  plt.show()


def plot_images(image_paths, positions, size=45):
  '''
  @arg paths arr: a list of strings, each of which specifies the path to an image on disk
  @arg positions numpy.ndarray: an array with shape (len(paths), 2) that specifies
    the x, y coordinates of each image
  @kwarg size int: the width of each image
  @returns matplotlib.pyplot: a scatterplot of the input images
  '''
  # unpack the x and y dimensions of each image
  x, y = positions.T

  # create the plot
  fig, ax = plt.subplots(figsize=(18, 10))

  # make the background black
  ax.set_facecolor('black')

  # add points at each position
  ax.scatter(x, y)

  # iterate over each image and its positions
  for x_val, y_val, path in zip(x, y, image_paths):

    # red in the image
    im = load_img(path)

    # get the image size
    w, h = im.size

    # resize the image
    im = im.resize((size, int(size*h/w)))

    # transform the image to an array and scale the pixel values
    im = img_to_array(im) / 255

    # plot the image
    ax.add_artist(AnnotationBbox(OffsetImage(im), (x_val, y_val), frameon=False))

  # show the plot
  plt.show()


def upload_output(email='', username='', token=''):
  '''
  Upload all contents in `./output` to github pages for viewing
  '''
  # create a new repository for this visualization
  guid = str(uuid.uuid1())
  g = Github(token)
  user = g.get_user()
  repo = user.create_repo(guid)

  # push content to gh-pages branch of repository
  os.system('git init')
  os.system('git config --global user.email "{}"'.format(email))
  os.system('git config --global user.name "{}"'.format(username))
  os.system('git remote add webhost https://{}:{}@github.com/{}/{}.git'.format(username, token, username, guid))
  os.system('git checkout -b gh-pages')
  os.system('git add output')
  os.system('git commit -m "add {}"'.format(guid))
  os.system('git push webhost gh-pages')

  # identify the url where the page will be available
  url = 'https://{}.github.io/{}/output/index.html'.format(username, guid)

  # inform the user of the url
  print(' * your plot will soon be available at', url)