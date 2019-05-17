# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:42:41 2019

@author: Administrator
"""

from PIL import Image
pil_im = Image.open('timg.jpg')
box = (100,100,400,400)
#crop() 方法可以从一幅图像中裁剪指定区域
region = pil_im.crop(box)
region.show()