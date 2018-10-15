# -*- coding: utf-8 -*-
# by wei.l.c

import os
from urllib import request

def Schedule(a,b,c):
    """
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    """
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)
    
def getImg(imglist, namelist):
    """
    图片获取-批量下载
    imglist  图片地址
    namelist 保存位置
    """
    for i in range(len(imglist)):
        if (os.path.exists(os.path.dirname(namelist[i])) == False):
            print(i,os.path.dirname(namelist[i])+'不存在')
        else:
            print(i,namelist[i] + '...')
            request.urlretrieve(imglist[i], namelist[i], Schedule)

def getImg_1(imglist, namelist):
    """
    图片获取-单个下载
    imglist  图片地址
    namelist 保存位置
    """
    print('url:' + imglist)
    
    if (os.path.exists(os.path.dirname(namelist)) == False):
        print(os.path.dirname(namelist)+'不存在')
    else:
        request.urlretrieve(imglist, namelist, Schedule)

def getImg_2(imglist, namelist):
    """
    图片获取-单个下载
    imglist  图片地址
    namelist 保存位置
    """
    print('url:' + imglist)
    
    if (os.path.exists(os.path.dirname(namelist)) == False):
        print(os.path.dirname(namelist)+'不存在')
    else:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
        headers = {'User-Agent' : user_agent}
        req = request.Request(url=imglist, headers=headers)
        
        print(namelist)
        with request.urlopen(req) as web:
            with open(namelist, 'wb') as outfile: # 为保险起见使用二进制写文件模式，防止编码错误
                outfile.write(web.read())