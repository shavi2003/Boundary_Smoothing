from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import watershed
from skimage.segmentation import mark_boundaries, find_boundaries, watershed
from skimage.filters import sobel
from skimage.segmentation import slic

#reading the image and showing in grayscale
myimage = io.imread('15746.png')
plt.imshow(myimage, cmap=plt.cm.gray)
plt.show()

#histogram showing frequency of gray values in picture
hist = np.histogram(myimage, bins= np.arange(0,256))
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(8,3))
ax1.imshow(myimage, cmap=plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.plot(hist[1][:-1], hist[0], lw=2)
ax2.set_title('histogram of grey values')
plt.show()


selected_pixles = []
for i in hist[1][:-1]:
    if hist[0][i] >= 700:
        selected_pixles.append(i)

#using sobel filter
image = sobel(myimage)
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('elevation_map')

#showing markers
markers = np.zeros_like(myimage)
markers[myimage < min(selected_pixles)] = 1
markers[myimage > max(selected_pixles)] = 2
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(markers, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('markers')

#based on markers using watershed segmentation
seg = watershed(image, markers=markers)
#print(np.shape(seg[1]))
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(seg, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('segmentation')
#plt.show()


'''bound = mark_boundaries(seg,seg, mode='thick')
#print(np.shape(bound[0]))
plt.imshow(bound, cmap=plt.cm.gray)
plt.show()'''

#show up boundaries
bounder = find_boundaries(seg, mode='thick').astype(np.uint8)
print(bounder)