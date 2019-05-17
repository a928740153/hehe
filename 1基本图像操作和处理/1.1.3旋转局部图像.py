# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:53:33 2019

@author: Administrator
"""

from PIL import Image
pil_im = Image.open('timg.jpg')
box = (100,100,400,400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
pil_im.show()