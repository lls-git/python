# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 12:09:14 2018

@author: Wei.l.c
"""

import os
import pandas as pd

def chkDir(fname):
    if (os.path.exists(os.path.dirname(fname)) == False):
        print('自动创建：'+os.path.dirname(fname))
        os.mkdir(os.path.dirname(fname));


def chkData(geo, fcreate):
    if fcreate:
        geo=pd.DataFrame(columns=['index','date','biaoti','zuozhe','jianjie','downurl','down_htm','down_pdf','ref'])
        fcreate=False
        
    return geo, fcreate
    
    
def chkData_geo(geo, fcreate):
    if fcreate:
        geo=pd.DataFrame(columns=['index','date','biaoti','zuozhe','jianjie','downurl','downcount'])
#        geo=pd.DataFrame(columns=['index','date','biaoti','zuozhe','jianjie','downurl','down_htm','down_pdf','ref'])
        fcreate=False
        
    return geo, fcreate