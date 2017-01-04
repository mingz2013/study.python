# -*- coding: UTF-8 -*-

import httplib

def GetHtmlSource_Post(getString):
    htmSource = ""
    
    try:
        url = httplib.urlsplit("http://app.sipo.gov.cn:8080")
        conn = httplib.HTTPConnection(url.netloc)
        conn.connect()
        conn.putrequest("POST", "/sipo/zljs/hyjs-jieguo.jsp")
        conn.putheader("Content-Length", len(getString))
        conn.putheader("Content-Type", "application/x-www-form-urlencoded")
        conn.putheader("Connection", " Keep-Alive")
        conn.endheaders()
        conn.send(getString)
        f = conn.getresponse()
        if not f:
            raise socket.error, "timed out"
        
        htmSource = f.read()
        f.close()
        conn.close()
         
        return htmSource
        
    except Exception(), err:
        
        trackback.print_exec()
        conn.close()
        
        
    return htmSource
    
getString = 'this is a string'
html = GetHtmlSource_Post(getString)
print html
