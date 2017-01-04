# -*- coding: UTF-8 -*-
'''
伪装成浏览器访问
某些网站反感爬虫的到访，于是对爬虫一律拒绝请求
这时候我们需要伪装成浏览器，这可以通过修改http包中的header来实现
'''
#…
import urllib
import urllib2

postdata=urllib.urlencode({
    'username':'XXXXX',
    'password':'XXXXX',
    'continueURI':'http://www.verycd.com/',
    'fk':'fk',
    'login_submit':'登录'
})

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

url = 'http://secure.verycd.com/signin/*/http://www.verycd.com/'

req = urllib2.Request(
    url,
    postdata,
    headers
)

result = urllib2.urlopen(req).read()

print result


#...
