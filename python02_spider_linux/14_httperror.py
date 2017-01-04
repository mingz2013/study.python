# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError  

someurl = 'http://www.google.com'

req = Request(someurl)  
  
try:  
  
    response = urlopen(req)  
  
except URLError, e:  
  
    if hasattr(e, 'reason'):  
  
        print 'We failed to reach a server.'  
  
        print 'Reason: ', e.reason  
  
    elif hasattr(e, 'code'):  
  
        print 'The server couldn\'t fulfill the request.'  
  
        print 'Error code: ', e.code  
  
else:  
  
    print 'everything is fine'  
