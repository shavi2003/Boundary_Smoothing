from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import watershed
from skimage.segmentation import mark_boundaries, find_boundaries, watershed
from skimage.filters import sobel
from skimage.util import img_as_float
from skimage.segmentation import slic
 
arguments = {
	"image": "Lenna.png"
}

#loading and opening an image for usage
image = Image.open(arguments["image"])



# Opening the image (R prefixed to string
# in order to deal with '\' in paths)
#image = Image.open(r"Lenna.png")
 
# Converting image to GrayScale otherwise the programme won't work
image = image.convert("L")
 
# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)
 
# Saving the Image Under the name Edge_Sample.png
image.save(r"edged_Lenna_sample.png")