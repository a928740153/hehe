# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:29:33 2019

@author: Administrator
"""

from PIL import Image
pil_im = Image.open('timg.jpg')
pil_im = Image.open('timg.jpg').convert('L')
pil_im.show()