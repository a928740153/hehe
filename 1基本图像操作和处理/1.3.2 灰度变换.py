# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:14:13 2019

@author: Administrator
"""

from PIL import Image
from numpy import *
im = array(Image.open('ting.jpg').convert('L'))
im2 = 255 - im # 对图像进行反相处理
im3 = (100.0/255) * im + 100 # 将图像像素值变换到 100...200 区间
im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到的图像

figure()
subplot(1,4,1)
imshow(im)
subplot(1,4,2)
imshow(im2)
subplot(1,4,3)
imshow(im3)
subplot(1,4,4)
imshow(im4)

show()


print(int(im.min()), int(im.max()))
print(int(im2.min()), int(im2.max()))
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))