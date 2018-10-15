# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 12:03:47 2018

@author: Wei.l.c
"""

from getHtml import getHtml
from bs4 import  BeautifulSoup
from getImg import getImg_2
from chkDir import chkDir
from chkName import chkName
import os,time,random

def getPapers_gpp(url):
    html=getHtml(url,0)
    soup=BeautifulSoup(html,'lxml')
    
    tmp=soup.findAll(["a"])
    papers=[]
    for ii in tmp:
        j=str(ii)
        if j.find("J_WenZhang")>=0:
            soup1=BeautifulSoup(j,'lxml')
            jj=str(soup1.a.string)
            if (not jj.isspace()) and (jj!="None"):
                papers.append(j[j.find("volumn_")+len('volumn_'):j.find(".shtml")])
    
    return papers
   
    
def getPapers_ogp(url):
    html=getHtml(url,0)
    soup=BeautifulSoup(html,'lxml')
    
    tmp=soup.findAll(["a"])
    papers=[]
    for ii in tmp:
        j=str(ii)
        if j.find("J_WenZhang")>=0:
            soup1=BeautifulSoup(j,'lxml')
            jj=str(soup1.a.string)
            if (not jj.isspace()) and (jj!="None"):
                papers.append(j[j.find("volumn_")+len('volumn_'):j.find(".shtml")])
    
    return papers
    
    
def getPapers_geo(url):
    html=getHtml(url,0)
    soup=BeautifulSoup(html,'lxml')
    
    tmp=soup.findAll(["td"])
    papers=[]
    for ii in tmp:
        j=str(ii)
        if j.find("href")>=0:
            papers.append(j[j.find("volumn_")+7:j.find("shtml")-1])
    
    return papers
    
    
def getPaper(geo, oname, save_url, burl, biaoti, total, i, date, zuozhe, jianjie, downurl, down_htm, down_pdf, ref):
    print('共('+ str(i) + '-' + str(total) +'):' + str(len(biaoti)) + '篇')
    
    for j in range(0,len(biaoti)):
        print('第' + str(j+1) + '篇')
        geo.loc[total]=[i,date,biaoti[j].strip(),zuozhe[j].strip(),jianjie[j].strip(),downurl[j].strip(),down_htm[j].strip(),down_pdf[j].strip(),ref[j].strip()]
        
        biaoti[j]=chkName(biaoti[j])
        fname=save_url+'\\'+date+'\\'+biaoti[j].strip()+'.pdf'
        chkDir(fname)
        
        if j not in burl:
            if os.path.exists(fname): # 存在则不再下载
                print(fname+' 已存在')
            else:
                getImg_2(downurl[j].strip(),fname)
                time.sleep(int(random.uniform(3,5))); # 随机暂停一下
        
        geo.to_csv(oname,sep=',',index=False)
        
        total=total+1
        
    return geo, total
    
    
def getPaper_geo(geo, oname, save_url, burl, biaoti, total, i, date, zuozhe, jianjie, downurl, down_pdf):
    print('共('+ str(i) + '-' + str(total) +'):' + str(len(biaoti)) + '篇')
    
    for j in range(0,len(biaoti)):
        print('第' + str(j+1) + '篇')
        geo.loc[total]=[i,date,biaoti[j].strip(),zuozhe[j].strip(),jianjie[j].strip(),downurl[j].strip(),down_pdf[j].strip()]
#        geo.loc[total]=[i,date,biaoti[j].strip(),zuozhe[j].strip(),jianjie[j].strip(),downurl[j].strip(),down_htm[j].strip(),down_pdf[j].strip(),ref[j].strip()]
        
        biaoti[j]=chkName(biaoti[j])
        fname=save_url+'\\'+date+'\\'+biaoti[j].strip()+'.pdf'
        chkDir(fname)
        
        if j not in burl:
            if os.path.exists(fname): # 存在则不再下载
                print(fname+' 已存在')
            else:
                getImg_2(downurl[j].strip(),fname)
                time.sleep(int(random.uniform(3,5))); # 随机暂停一下
        
        geo.to_csv(oname,sep=',',index=False)
        
        total=total+1
        
    return geo, total