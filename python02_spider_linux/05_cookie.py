# -*- coding: UTF-8 -*-

import urllib2, cookielib

cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())

opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)

urllib2.install_opener(opener)

content = urllib2.urlopen('http://www.baidu.com').read()

print content
''''
是的没错，如果想同时用代理和cookie，那就加入proxy_support然后operner改为
opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
'''
