# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:04:48 2019

@author: Administrator
"""

from PIL import Image
pil_im = Image.open('timg.jpg')
out = pil_im.rotate(45)
out.show()