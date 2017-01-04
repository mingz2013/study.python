# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError  

someurl = 'http://www.baidu.com'

req = Request(someurl)  
  
try:  
  
    response = urlopen(req)  
  
except HTTPError, e:  
  
    print 'The server couldn\'t fulfill the request.'  
  
    print 'Error code: ', e.code  
  
except URLError, e:  
  
    print 'We failed to reach a server.'  
  
    print 'Reason: ', e.reason  
  
else:  
  
    print 'everything is fine' 
