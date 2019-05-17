# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:49:23 2019

@author: Administrator
"""

from PIL import Image
import os
#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
filelist=os.listdir('filelist/')
for infile in filelist:
#os.path.splitext分离文件名与扩展名
    outfile = os.path.splitext(infile)[0] + ".jpeg"
    if infile != outfile:
        try:
            Image.open('filelist/'+infile).save(outfile)
        except IOError:
            print ("cannot convert", infile)