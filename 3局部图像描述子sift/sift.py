# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:59:23 2019

@author: Administrator
"""

def process_image(imagename,resultname,params="--edge-thresh 10 --peak-thresh 5"):
#""" 处理一幅图像，然后将结果保存在文件中 """
    if imagename[-3:] != 'pgm':
    # 创建一个 pgm 文件
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'
    cmmd = str("sift "+imagename+" --output="+resultname+" "+params)
    os.system(cmmd)
    print('processed', imagename, 'to', resultname)

def read_features_from_file(filename):
#""" 读取特征属性值，然后将其以矩阵的形式返回 """
    f = loadtxt(filename)
    return f[:,:4],f[:,4:] # 特征位置，描述子
def write_features_to_file(filename,locs,desc):
#""" 将特征位置和描述子保存到文件中 """
    savetxt(filename,hstack((locs,desc)))

def plot_features(im,locs,circle=False):
#""" 显示带有特征的图像
#输入：im（数组图像），locs（每个特征的行、列、尺度和朝向）"""
    def draw_circle(c,r):
        t = arange(0,1.01,.01)*2*pi
        x = r*cos(t) + c[0]
        y = r*sin(t) + c[1]
        plot(x,y,'b',linewidth=2)
        imshow(im)
if circle:
    for p in locs:
    draw_circle(p[:2],p[2])
else:
    plot(locs[:,0],locs[:,1],'ob')
axis('off')