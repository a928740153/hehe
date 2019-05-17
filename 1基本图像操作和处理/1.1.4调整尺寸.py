# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:55:17 2019

@author: Administrator
"""

from PIL import Image
pil_im = Image.open('timg.jpg')
out = pil_im.resize((128,128))
out.show()