# -*- coding: utf8 -*-
import urllib2,urllib,sys
"""
使用POST提交Form数据
1.编码还是使用urlencode
2.不必要使用字符串连接
3.使用urlopen的data参数
例子无法运行,原因是www.google.com只支持GET方式,没有提供POST方式
"""

url = "http://www.google.com/search"
search = urllib.urlencode([('q','python')])

req = urllib2.Request(url)
fd = urllib2.urlopen(req,search)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
