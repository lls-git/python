# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:55:25 2018

@author: Wei.l.c
"""

from getHtml import getHtml
from getPaper import getPapers_ogp,getPaper
from chkDir import chkData
import pandas as pd
from bs4 import  BeautifulSoup

cur_url='http://www.ogp-cn.com.cn/CN/volumn/current'
main_url='http://www.ogp-cn.com.cn/CN/article/showOldVolumn.do'
bash_url='http://www.ogp-cn.com.cn/CN/volumn/volumn_'
bashurl='_abs.shtml'
down_url='http://www.ogp-cn.com.cn/CN'
save_url=r'D:\Paper\石油地球物理勘探'
save_name='ogp.csv'

def getPapers(url,spath,i,geo,total,fcreate=False):
    html=getHtml(url,0)
    
    soup=BeautifulSoup(html,'lxml')
    
    tmp=soup.findAll(["a"])
    ref=[]
#    biaoti=[]
#    zuozhe=[]
    downurl=[]
    downurlP=[]
    burl=[]
    flag=0
    for ii in tmp: # 参考文献
        j=str(ii)
        if j.find("onclick")>=0:
            ref.append(j[j.find("('")+2:j.find("')")-4]+';')
#            biaoti.append(j[j.find(".")+2:j.find("[J]")])
#            zuozhe.append(j[j.find("('")+2:j.find(".")])
            
        if j.find("attachType=PDF")>=0:
            downurlP.append(down_url+j[j.find("href=")+8:j.find("<u>PDF")-2].replace('amp;',''))
        if j.find("J_VM")>=0:
            flag=flag+1
            if flag==2:
                if j.find("attachType=HTML")<0:
                    burl.append(len(downurl))
                downurl.append(down_url+(j[j.find("href=")+8:j.find("<u>HTML")-2].replace('amp;','').replace('HTML','PDF')))
#                else:
#                    downurlP.index(biaoti)
                flag=0
            
    tmp=soup.findAll(["b"])
    biaoti=[]
    for ii in tmp: # 标题
        j=str(ii)
        biaoti.append(j[j.find("<b>")+3:j.find("</b>")])
    if('' in biaoti): # 空标题
        tmp=soup.findAll(["p"])
#        for ii in tmp:
#            j=str(ii)
        j=str(tmp[1])
        biaoti[biaoti.index('')]=j[j.find("Verdana")+9:j.find("</font>")]
        
    tmp=soup.findAll(["font"])
    down_htm=[]
    down_pdf=[]
    flag=0
    for ii in tmp: # 下载次数
        j=str(ii.string).strip()
        if j.isdigit():
            flag=flag+1
            if flag==1:
                down_htm.append(j)
            elif flag==2:
                down_pdf.append(j)
                flag=0
        
    tmp=soup.findAll(["td"])
    zuozhe=[]
    jianjie=[]
    flag=0
    for ii in tmp: # 摘要
        soup1=BeautifulSoup(str(ii),'lxml')
        j=str(soup1.td.string)
        if j!="None":
            if j.isdigit() or flag>0:
                flag=flag+1
                if j.isdigit() and flag==3: #获取失败
                    flag=1
                    jianjie.append('')
                elif j.isdigit() and flag==2: #获取失败
                    flag=1
                    jianjie.append('')
                    zuozhe.append('')
                elif flag==3:
                    flag=0
                    jianjie.append(j)
                elif flag==2:
                    zuozhe.append(j)
    for ii in range(len(jianjie),len(biaoti)):
        jianjie.append('')
    
    tmp=soup.findAll(["strong"])
    tmp=str(tmp[0]).split('：')[1][0:-9] # 出版日期
    
    geo, fcreate=chkData(geo, fcreate)  
    geo, total=getPaper(geo, spath+'\\'+save_name, spath, burl, biaoti, total, i, tmp, zuozhe, jianjie, downurl, down_htm, down_pdf, ref)
    
    return geo, fcreate, total
    
    
def getPapers_all(spath=save_url,spage=0,fcreate=False):
    papers=getPapers_ogp(main_url)
    papers=papers[3:-1]
    papers.sort()
    
    if fcreate:
        geo=[]
        total=0
    else:
        geo=pd.read_csv(spath+'\\'+save_name,encoding='gbk')
        total=geo.shape[0]
    
#    for i in range(1228,1229): #(1134,1484) 1154 1179 1182 1188 1245 1375 1421 1426-1429 1439 1457 1463
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