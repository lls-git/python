# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 11:19:00 2018

@author: Wei.l.c
"""

def chkName(fname):
    if fname.find('<em>')>=0: # 加大
        fname=fname.replace('<em>','')
        print('replace <em> '+ fname)
    if fname.find('</em>')>=0:
        fname=fname.replace('</em>','')
        print('replace </em> '+ fname)
    if fname.find('<_em>')>=0:
        fname=fname.replace('<_em>','')
        print('replace <_em> '+ fname)
    if fname.find('<EM>')>=0:
        fname=fname.replace('<EM>','')
        print('replace <EM> '+ fname)
    if fname.find('</EM>')>=0:
        fname=fname.replace('</EM>','')
        print('replace </EM> '+ fname)
    if fname.find('<_EM>')>=0:
        fname=fname.replace('<_EM>','')
        print('replace <_EM> '+ fname)
        
    if fname.find('<sub>')>=0: # 下标
        fname=fname.replace('<sub>','')
        print('replace <sub> '+ fname)
    if fname.find('</sub>')>=0:
        fname=fname.replace('</sub>','')
        print('replace </sub> '+ fname)
    if fname.find('<_sub>')>=0:
        fname=fname.replace('<_sub>','')
        print('replace <_sub> '+ fname)
    if fname.find('<SUB>')>=0:
        fname=fname.replace('<SUB>','')
        print('replace <SUB> '+ fname)
    if fname.find('</SUB>')>=0:
        fname=fname.replace('</SUB>','')
        print('replace </SUB> '+ fname)
    if fname.find('<_SUB>')>=0:
        fname=fname.replace('<_SUB>','')
        print('replace <_SUB> '+ fname)
    
    if fname.find('<sup>')>=0: # 上标
        fname=fname.replace('<sup>','')
        print('replace <sup> '+ fname)
    if fname.find('</sup>')>=0:
        fname=fname.replace('</sup>','')
        print('replace </sup> '+ fname)
    if fname.find('<_sup>')>=0:
        fname=fname.replace('<_sup>','')
        print('replace <_sup> '+ fname)
    if fname.find('<SUP>')>=0:
        fname=fname.replace('<SUP>','')
        print('replace <SUP> '+ fname)
    if fname.find('</SUP>')>=0:
        fname=fname.replace('</SUP>','')
        print('replace </SUP> '+ fname)
    if fname.find('<_SUP>')>=0:
        fname=fname.replace('<_SUP>','')
        print('replace <_SUP> '+ fname)
        
    if fname.find('<br>')>=0:
        fname=fname.replace('<br>','')
        print('replace <br> '+ fname)
    if fname.find('</br>')>=0:
        fname=fname.replace('</br>','')
        print('replace </br> '+ fname)
    if fname.find('<_br>')>=0:
        fname=fname.replace('<_br>','')
        print('replace <_br> '+ fname)
    if fname.find('<BR>')>=0:
        fname=fname.replace('<BR>','')
        print('replace <BR> '+ fname)
    if fname.find('</BR>')>=0:
        fname=fname.replace('</BR>','')
        print('replace </BR> '+ fname)
    if fname.find('<_BR>')>=0:
        fname=fname.replace('<_BR>','')
        print('replace <_BR> '+ fname)
        
    if fname.find(':')>=0: # 文件名不允许包含
        fname=fname.replace(':','_')
        print('replace : '+ fname)
        
    if fname.find('?')>=0:
        fname=fname.replace('?','_')
        print('replace ? '+ fname)
        
    if fname.find('/')>=0:
        fname=fname.replace('/','_')
        print('replace / '+ fname)
        
    if fname.find('\\')>=0:
        fname=fname.replace('\\','_')
        print('replace \\ '+ fname)
        
    if fname.find('|')>=0:
        fname=fname.replace('|','_')
        print('replace | '+ fname)
        
    if fname.find('<')>=0:
        fname=fname.replace('<','_')
        print('replace < '+ fname)
    
    if fname.find('>')>=0:
        fname=fname.replace('>','_')
        print('replace > '+ fname)
        
    if fname.find('?')>=0:
        fname=fname.replace('?','_')
        print('replace ? '+ fname)
    
    if fname.find('"')>=0:
        fname=fname.replace('"','_')
        print('replace " '+ fname)
       
    if fname.find('*')>=0:
        fname=fname.replace('*','_')
        print('replace * '+ fname)
        
    return fname