# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:35:37 2019

@author: Administrator
"""

from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('ting.jpg').convert('L'))
# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
#x轴和y轴的单位长度相同
axis('equal')
#关闭所有坐标轴线、刻度标记和标签
axis('off')
figure()
hist(im.flatten(),128)
show()