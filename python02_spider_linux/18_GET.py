# -*- coding: UTF-8 -*-

import httplib

def GetHtmlSource_Get(htmurl):
    htmSource = ""
    
    try:
        
        urlx = httplib.urlsplit(htmurl)
        conn = httplib.HTTPConnection(urlx.netloc)
        conn.connect()
        conn.putrequest("GET", htmurl, None)
        
        conn.putheader("Content-Length", 0)
        conn.putheader("Connection", "close")
        conn.endheaders()
        
        res = conn.getresponse()
        htmSource = res.read()
        
    except Exception(), err:
        trackback.print_exec()
        conn.close()
        
        
    return htmSource

htmurl = 'http://www.baidu.com'
html = GetHtmlSource_Get(htmurl)
print html
