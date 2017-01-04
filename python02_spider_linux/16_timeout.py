# -*- coding: UTF-8 -*-

import socket  
import urllib2
  
# 以秒计算的超时时间  
timeout = 10  
socket.setdefaulttimeout(timeout)  
  
# 这个调用urllib.request.urlopen 使用我们在socket模型里设置的默认超时时间。  
req = urllib2.Request('http://www.voidspace.org.uk')  
response = urllib2.urlopen(req)

print response.read()
