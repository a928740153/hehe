# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:02:15 2019

@author: Administrator
"""

from numpy import *
from PIL import Image
from pylab import *
from imtools import pca
im2 = '666.jpg'

imlist = [im2,im2,im2,im2,im2,im2,im2,im2]

im = array(Image.open(imlist[0]))
imshow(im)
m,n = im.shape[0:2]
imnbr = len(imlist)
immatrix = array([array(Image.open(im).convert('L')).flatten() for im in imlist],'f')
print(imlist)
# 执行PCA操作
V,S,immean = pca(immatrix)
# 显示一些图像
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(immean.reshape(m, n))
    imshow(V[i].reshape(m,n))
show()