# -*- coding: utf8 -*-
import urllib2,urllib,sys
"""
使用GET在百度搜索引擎上查询
在百度的搜索条中随便输入一些内容,会有w和cl两项构成GET串
此例演示如何生成GET串,并进行请求.
"""

url = "http://www.baidu.com/s"
search = [('w','python'),('cl','3')]
getString = url + "?" + urllib.urlencode(search)

req = urllib2.Request(getString)
fd = urllib2.urlopen(req)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data) 
