# -*- coding: UTF-8 -*-

import urllib2

req = urllib2.Request('http://www.pretend_server.org')  
  
try: urllib2.urlopen(req)  

except urllib2.URLError, e:  
  
   print e.reason  
  
 
  
#[Errno 2] No such file or directory
 
