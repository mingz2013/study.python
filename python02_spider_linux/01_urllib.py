# -*- coding: UTF-8 -*-
import urllib
 
' 获取web页面内容并返回'
'''
def getWebPageContent(url):
    f = urllib.urlopen(url)
    data = f.read()
    f.close()
    return data
 '''
#url = 'http://www.baidu.com'
#content = getWebPageContent(url)
'''
content = urllib.urlopen(url).read()
print content
'''
#print urllib.urlopen(url).read()

print urllib.urlopen("http://www.baidu.com").read()
'''
两行代码搞定，
第一行 引入urllib模块，
第二行 打开网址 并读取内容 然后打印
'''
