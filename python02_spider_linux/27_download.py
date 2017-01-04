#!/usr/local/bin/python3.2  
import urllib2,io,os,sys  
req=urllib2.Request("http://bbs.admin5.com/api.php?mod=js&bid=70")  
f=urllib2.urlopen(req)  
s=f.read()  
s=s.decode('gbk','ignore')  
mdir=sys.path[0]+'/'  
file=open(mdir+'admin5.txt','a','gbk')  
file.write(s)  
file.close()  
