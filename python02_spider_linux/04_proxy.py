# -*- coding: UTF-8 -*-
# 使用代理服务器
import urllib2

proxy_support = urllib2.ProxyHandler({'http':'http://XX.XX.XX.XX:XXXX'})

opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)

urllib2.install_opener(opener)

content = urllib2.urlopen('http://www.baidu.com').read()

print content
