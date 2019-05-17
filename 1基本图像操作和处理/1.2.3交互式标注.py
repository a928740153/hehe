# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:42:54 2019

@author: Administrator
"""

from PIL import Image
from pylab import *
im = array(Image.open('ting.jpg'))
imshow(im)
print('Please click 3 points')
#ginput提供了一个十字光标使我们能更精确的选择我们所需要的位置,并返回坐标值。
x = ginput(3)
print('you clicked:',x)
show()