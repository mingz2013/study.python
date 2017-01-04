#encoding=utf-8
#用python从百度获取亚马逊的商品ID
import web  
import tagparser  
db = web.database(dbn='mysql',user='root', pw='', db='webpy')  
count=0  
for i in range(10000,10):  
    url='http://www.baidu.com/s?wd=site%3Aamazon.cn%20dp%2FB&pn='+str(i)+'&tn=baiduhome_pg'  
    p=tagparser.TagParser()  
    p.fetchUrl(url)  
    for t in p.tagList:  
        a=t.find('dp/B0')  
        if a>0:  
            t=t[a+3:a+19]  
            s=t.split('"')  
            t=s[0]  
            s=t.split('/')  
            t=s[0]  
            db.insert('productid',productID=t,id=count)  
            count+=1  
print 'successed'  
