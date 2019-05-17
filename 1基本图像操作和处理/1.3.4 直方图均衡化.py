# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:56:24 2019

@author: Administrator
"""
from PIL import Image
from numpy import *
from pylab import *

def histeq(im,nbr_bins=256):
#""" 对一幅灰度图像进行直方图均衡化 """
# 计算图像的直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # 累计分布函数
    cdf = 255 * cdf / cdf[-1] # 归一化
# 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf

im = array(Image.open('666AA.jpg').convert('L'))
im2,cdf = histeq(im)
figure()
subplot(1,2,1)
imshow(im)
subplot(1,2,2)
imshow(im2)
show()