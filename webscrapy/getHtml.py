# -*- coding: utf-8 -*-
# by wei.l.c

import sys
import urllib
from urllib import request

def getHtml(url, flag=0):
    """
    网页获取
    flag 网页编码格式
    """
    print('url:' + url)
    
    html=''
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
        headers = {'User-Agent' : user_agent}
        
        req = request.Request(url=url, headers=headers)
        page = request.urlopen(req)
        html = page.read()
        
        if (html == 'null') or (html.strip()==''): # 有些网站不需要
            print('open & read Page error!')
        else:
            print('html:' + str(len(html)))
            #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"): # 是否具有该属性
            print('Code error:' + e.code)
        
        if hasattr(e,"reason"):
            print('Error reason:' + e.reason)
            
        sys.exit(-1)
    
    if flag==0:
        return html.decode('UTF-8')
    elif flag==1:
        return html.decode('GBK')
    else:
        return html
