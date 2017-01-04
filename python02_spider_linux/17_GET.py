# -*- coding: UTF-8 -*-

import urllib2
import socket

def GetHtmlSource(url):
    try:
    
        htmSource = ''
        
        req = urllib2.Request(url)
       
        fd = urllib2.urlopen(req)
        
        while 1:
            data = fd.read(1024)
            if not len(data):
                break
            
            htmSource += data

        fd.close()
  
        del fd
        del req
        
        #htmSource = htmSource.decode('cp936')
        #htmSource = formatStr(htmSource)
         
        return htmSource
        
    except socket.error, err:
        
        str_err =  "%s" % err
        return ""

url = 'http://www.baidu.com'
html = GetHtmlSource(url)
print html
