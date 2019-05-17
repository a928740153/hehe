# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:22:25 2019

@author: Administrator
"""

from PIL import Image
#pylab 模块是一款由python提供的可以绘制二维，三维数据的工具模块
from pylab import *

# 读取图像到数组中
im = array(Image.open('ting.jpg'))
# 绘制图像
imshow(im)
# 一些点
x = [100,100,400,400]
y = [200,500,200,500]
# 使用红色星状标记绘制点
plot(x,y,'r*')
# 绘制连接前两个点的线
plot(x[:2],y[:2])
# 添加标题，显示绘制的图像
title('Plotting: "ting.jpg"')
#关闭坐标轴
axis('off')
show()
