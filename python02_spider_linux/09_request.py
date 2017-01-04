# -*- coding: UTF-8 -*-
''''
urllib2用一个Request对象来映射你提出的HTTP请求,
在它最简单的使用形式中
  你将用你要请求的地址创建一个Request对象，
  通过调用urlopen并传入Request对象，
  将返回一个相关请求response对象，
  这个应答对象如同一个文件对象，
  所以你可以在Response中调用.read()。
'''

import urllib2  
  
req = urllib2.Request('http://www.baidu.com')
#还可一传入ftp file
#req = urllib2.Request('ftp://example.com/')
  
response = urllib2.urlopen(req)  
  
the_page = response.read()

print the_page
