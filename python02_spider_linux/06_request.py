# -*- coding: UTF-8 -*-

'''
表单的处理
登录必要填表，表单怎么填？首先利用工具截取所要填表的内容
比如我一般用firefox+httpfox插件来看看自己到底发送了些什么包
'''

#好的，有了要填写的数据，我们就要生成postdata

import urllib
import urllib2

postdata=urllib.urlencode({
    'username':'XXXXX',
    'password':'XXXXX',
    'continueURI':'http://www.verycd.com/',
    'fk':'fk',
    'login_submit':'登录'
})

#然后生成http请求，再发送请求：

req = urllib2.Request(
    url = 'http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data = postdata
)

result = urllib2.urlopen(req).read()

print result
