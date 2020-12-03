from keras.preprocessing.image import load_img, img_to_array, array_to_img
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import colorsys
import PIL

def plot_points_3d(im, width=50, labels=['Red', 'Green', 'Blue'], colorspace='rgb'):
  '''
  Plot points in a 3d space
  @arg im: numpy array with shape width, height, color_channels
  @kwarg width: integer indicating the width of the resized image; greater width => more points
  @kwarg labels: list of strings, one per x, y, z axes
  @kwarg colorspace: string rgb or hsv
  '''

  # check if this is a keras image rather than numpy array
  if isinstance(im, PIL.Image.Image): im = img_to_array(im)

  # conver the image to an array
  im = np.array(im)

  # slice off the alpha channel if present
  im = im[:,:,:3]

  # get the width, height, and color of the image
  w, h, c = im.shape

  # only resize the image if necessary
  if w > width:

    # specify the target width and height
    height = int(h/w * width)

    # convert to a keras image to resize then back to array
    im = img_to_array(array_to_img(im).resize((width, height)))

    # get the size of the new image
    w, h, c = im.shape

  # specify the figure size for this image
  fig = plt.figure(figsize=(8, 4))

  # add a 3d plot
  axis = fig.add_subplot(1, 1, 1, projection='3d')

  # flatten the image to get point positions
  flat = im.reshape(w * h, 3)
  r, g, b = flat.T

  # if this image is in a hsv colorspace, convert it to rgb
  if colorspace == 'hsv': im = hsv_to_rgb(im / np.max(im)) * 255.

  # flatten the hsv image
  flat = im.reshape(w * h, 3)

  # set the range of each axis
  axis.set_xlim(0, 255)
  axis.set_ylim(0, 255)
  axis.set_zlim(0, 255)

  # add the points to the plot
  axis.scatter(r, g, b, marker='.', c=flat/255)

  # add labels to the axes
  axis.set_xlabel(labels[0])
  axis.set_ylabel(labels[1])
  axis.set_zlabel(labels[2])

def sort_rows_by_color(arr):
  '''
  @arg arr: numpy array with shape (rows, colors_per_row, colors)
  @returns numpy array with shape (rows, colors_per_row, colors) where the colors
    in each row have been sorted in hsv space
  '''

  # ensure the array is a numpy array
  arr = np.array(arr)

  # create a list that will store the sorted colors
  l = []

  # iterate over each row in the array
  for i in arr:

    # convert this row to a list
    i = i.tolist()

    # sort the list with hsv values
    i.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))

    # append the sorted values to the list
    l.append(i)

  # convert the sorted list to an array
  return np.array(l)