# importing packages we need
from PIL import Image, ImageFilter
import numpy as np
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries, find_boundaries, watershed
from skimage.util import img_as_float, random_noise
from skimage.filters import butterworth, sobel
from skimage import io
#import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import feature
from scipy import ndimage as ndi


arguments = {
	"image": "Lenna.png"
}


# loading image to a file and then converting image to a floating point number
img = img_as_float(io.imread(arguments["image"]))
#img = rgb2gray(img)


#butterworth filter for boundary smoothing
img = butterworth(img, cutoff_frequency_ratio=0.5, high_pass=False, order=2.0, channel_axis=None)

    
#SLIC
segments = slic(img, n_segments = 100, compactness = 10, sigma = 5, enforce_connectivity = True)
bounder = find_boundaries(segments, mode='thick')



#plotting the figure and returning the image with boundaries
fig = plt.figure("Superpixels -- %d segments" % (150))
ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(img, segments))
plt.axis("off")    

# showing plots off
plt.show()