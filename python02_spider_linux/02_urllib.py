# -*- coding: UTF-8 -*-

import urllib
#使用urllib下载文件
url = 'http://www.baidu.com'
path = './/baidu.html'
urllib.urlretrieve(url,path)

# 打开文件 并打印
f = open(path, "r")
content = f.read()
f.close()
print content



#urllib.urlretrieve("http://www.baidu.com", ".//baidu.html")
#print open('.//baidu.html',"r")
