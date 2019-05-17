# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:36:36 2019

@author: Administrator
"""
from PIL import Image
pil_im = Image.open('timg.jpg')
#thumbnail() 方法接受一个元组参数（该参数指定生成缩略图的大小）
pil_im.thumbnail((128,128))
pil_im.show()



