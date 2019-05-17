from PIL import Image
from numpy import *
from scipy.ndimage import filters

#im = array(Image.open('1.jpg').convert('L'))
#im2 = filters.gaussian_filter(im,5)# 

im = array(Image.open('1.jpg'))
im2 = zeros(im.shape)
for i in range(3):
   im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im2 = uint(im2)
axis('off')
imshow(im2)
show()
