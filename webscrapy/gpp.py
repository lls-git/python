# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:55:25 2018

@author: Wei.l.c
"""

from getHtml import getHtml
from getPaper import getPapers_gpp,getPaper
from chkDir import chkData
import pandas as pd
from bs4 import  BeautifulSoup

cur_url='http://gpp.geophysics.cn/CN/volumn/current'
main_url='http://gpp.geophysics.cn/CN/article/showOldVolumn.do'
bash_url='http://gpp.geophysics.cn/CN/volumn/volumn_'
bashurl='_abs.shtml'
down_url='http://gpp.geophysics.cn/CN/article/downloadArticleFile.do?attachType=PDF&id='
save_url=r'D:\Paper\石油物探'
save_name='gpp.csv'

def getPapers(url,spath,i,geo,total,fcreate=False):
    html=getHtml(url,0)
    
    soup=BeautifulSoup(html,'lxml')
    
    tmp=soup.findAll(["a"])
    ref=[]
    downurl=[]
    burl=[]
    flag=0
    for ii in tmp: # 参考文献
        j=str(ii)
        if j.find("onclick")>=0:
            flag=flag+1
            if flag==1:
                ref.append(j[j.find("('")+2:j.find("')")-4].replace(',.','.')+';')
            elif flag>=2:
                if j.find("alert")>=0:
                    burl.append(len(downurl))
                    downurl.append(down_url)
                else:
                    downurl.append(down_url+j[j.find("PDF")+6:j.find("http")-3])
                flag=0
            
    tmp=soup.findAll(["b"])
    biaoti=[]
    flag=0
    for ii in tmp: # 标题
        flag=flag+1
        j=str(ii)
        if flag==2:# 出版日期
            date=j[j.find("</b>")-10:j.find("</b>")]
        elif flag>=3: # 刊出日期等
            biaoti.append(j[j.find("<b>")+3:j.find("</b>")])
    if('' in biaoti): # 空标题
        tmp=soup.findAll(["p"])
#        for ii in tmp:
#            j=str(ii)
        j=str(tmp[1])
        biaoti[biaoti.index('')]=j[j.find("Verdana")+9:j.find("</font>")]
    if int(i)==1370: # 异常
        biaoti.pop(4)
    if 'Hot!' in biaoti:
        biaoti.remove('Hot!')
        
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

    geo, fcreate=chkData(geo, fcreate)  
    geo, total=getPaper(geo, spath+'\\'+save_name, spath, burl, biaoti, total, i, date, zuozhe, jianjie, downurl, down_htm, down_pdf, ref)
    
    return geo, fcreate, total
    
    
def getPapers_all(spath=save_url,spage=0,fcreate=False):
    papers=getPapers_gpp(main_url)
    papers=papers[3:-1]
    papers.sort()
    
    if fcreate:
        geo=[]
        total=0
    else:
        geo=pd.read_csv(spath+'\\'+save_name,encoding='gbk')
        total=geo.shape[0]
    
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