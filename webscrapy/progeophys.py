# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 14:19:45 2018

@author: Wei.l.c
"""

from getHtml import getHtml
from getPaper import getPapers_geo,getPaper_geo
from chkDir import chkData_geo
from lxml import etree
import re
import pandas as pd

cur_url='http://www.progeophys.cn/CN/1004-2903/current'
main_url='http://www.progeophys.cn/CN/1004-2903/home.shtml'
bash_url='http://www.progeophys.cn/CN/volumn/volumn_'
bashurl='.shtml'
down_url='http://www.progeophys.cn/CN/article/downloadArticleFile.do?attachType=PDF&id='
save_url=r'D:\Paper\中国地球物理学进展'
save_name='geo.csv'

def getPapers(url,spath,i,geo,total,fcreate=False):
    html=getHtml(url,0)
    
    burl=[]

    reg='<a href="javascript:;" onclick="lsdy1'+'(.*?)'+''','http://www.progeophys.cn'''
    downno=re.findall(reg,html)
    downurl=[]
    for j in downno:
        tmp=j.split(',')
        tmp=tmp[1]
        downurl.append(down_url+tmp[1:-1])
    reg='<a target="_blank".*?>'+'(.*?)'+'</a>'
    biaoti=re.findall(reg,html)
    reg='<div class="zuozhe">'+'(.*?)'+'</div>'
    zuozhe=re.findall(reg,html)
    
    html=etree.HTML(html)
    chuban=html.xpath('//div[@class="chuban"]/span/text()')
#    biaoti=html.xpath('//li/div[@class="biaoti"]/a/text()') #存在特殊字符情况
#    zuozhe=html.xpath('//li/div[@class="zuozhe"]/text()') #存在空值情况
    jianjie=html.xpath('//li/div[@class="jianjie"]/text()')
    downcount=html.xpath('//li/div/span/b/text()')
    
    tmp=chuban[1].split(' ')
    tmp=tmp[1] # 出版日期
    
    geo, fcreate=chkData_geo(geo, fcreate)  
    geo, total=getPaper_geo(geo, spath+'\\'+save_name, spath, burl, biaoti, total, i, tmp, zuozhe, jianjie, downurl, downcount)
    
    return geo, fcreate, total
    
    
def getPapers_all(spath=save_url,spage=0,fcreate=False):
    papers=getPapers_geo(main_url)
    papers.sort()
    for i in papers:
        print(i)
    
    if fcreate:
        geo=[]
        total=0
    else:
        geo=pd.read_csv(spath+'\\'+save_name,encoding='gbk')
        total=geo.shape[0]

#    for i in range(233,234): #(1,150)
    for i in papers:
        if int(i)<spage:
            continue
        
        url=bash_url+str(i)+bashurl
        geo, fcreate, total=getPapers(url,spath,i,geo,total,fcreate)

        
def getPapers_cur(spath=save_url,fcreate=False):
    if fcreate:
        geo=[]
        total=0
    else:
        geo=pd.read_csv(spath+'\\'+save_name,encoding='gbk')
        total=geo.shape[0]
    
    url=cur_url+bashurl
    geo, fcreate, total=getPapers(url,spath,9999,geo,total,fcreate)