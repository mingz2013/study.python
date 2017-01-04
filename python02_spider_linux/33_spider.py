#-*- coding: UTF-8 -*-



#Program: a small spider written in python

#Author : liuhaobupt

#Date : 2009-10-29

#Version: v1.0



from Utility import PriorityQueue,Parser

import urllib2

import sys

import os

import string

import socket



def updatePriQueue(priQueue,url,beginurl):

    extraPrior = url.endswith('.html') and 20 or 0

    extraBeginUrl = beginurl in url and 5 or 0

    extraLevel = string.find(url,'/')

    schemeType = ['http://','ftp://','file://']

    flag = 0

    for type in schemeType:

        if url.startswith(type):

            flag = 1

    if not flag:

        return

    item = priQueue.getitem(url)

    if item:

        newitem = (item[0]+1+extraPrior+extraBeginUrl-extraLevel,item[1])

        priQueue.remove(item)

        priQueue.push(newitem)

    else:

        priQueue.push((1+extraPrior+extraBeginUrl-extraLevel,url))





def analyseHtml(url,html,priQueue,downlist,beginurl):

    p = Parser(html)

    for v in p.links:

        if not downlist.count(v):

            updatePriQueue(priQueue,v,beginurl)



       



def downloadUrl(id,url,priQueue,downlist,downFolder,beginurl):

    downFileName = downFolder+'/%d.html'%(id,)

    print 'downloading',url,'as',downFileName

   

    socket.setdefaulttimeout(2)

    try:

        fp = urllib2.urlopen(url)

    except:

        print '[failed]'

        return 0

    else:

        downlist.push(url)

        op = open(downFileName,"wb")

        try:

            html = fp.read()

        except:

            op.close()

            fp.close()

            print '[failed]'

            return 0

        else:

            print '[success]'

            op.write(html)

            op.close()

            fp.close()



            analyseHtml(url,html,priQueue,downlist,beginurl)

            return 1



def spider(beginurl,pages,downFolder):



    priQueue = PriorityQueue() #保存待下载url的链接

    downlist = PriorityQueue() #已下载url集合，防止重复下载

    priQueue.push((1,beginurl))

    i = 0

    while not priQueue.empty() and i <pages:

        k,url = priQueue.pop()

        if downloadUrl(i+1,url,priQueue,downlist,downFolder,beginurl):

            i+=1



    print '\nDownload',i,'pages.'



def main():

    beginurl = sys.argv[1] #初始的url地址

    pages = string.atoi(sys.argv[2]) #抓取网页的数目

    downloadFolder = sys.argv[3] #指定保存网页的文件夹

    if not os.path.isdir(downloadFolder):

        os.mkdir(downloadFolder)



    spider(beginurl,pages,downloadFolder)



if __name__ =='__main__':

    main()



 



#file:Utility.py



import bisect

import string

import re



class PriorityQueue(list):

    def __init__(self):

        list.__init__(self)

        self.map = {}



    def push(self,item):

        if self.count(item) == 0:

            bisect.insort(self,item)

            self.map[item[1]] = item



    def pop(self):

        r = list.pop(self)

        del self.map[r[1]]

        return r



    def getitem(self,url):

        if self.map.has_key(url):

            return self.map[url]

        else:

            return None



    def empty(self):

        return len(self) == 0



    def remove(self,item):

        list.remove(self,item)

        del self.map[item[1]]



    def count(self,item):

        if len(self) == 0:

            return 0

        left = 0

        right = len(self)-1

        mid = -1

        while left<=right:

            mid = (left+right)/2

            if self[mid] < item:

                left = mid+1

            elif self[mid] >item:

                right= mid-1

            else:

                break

        return self[mid] == item and 1 or 0

       

       



class Parser():

    def __init__(self,html):

        self.links = []

        re_pattern = "\shref=[\"']?([^\"'\s>]+)[\"'\s>]"

        re_href = re.compile(re_pattern,re.IGNORECASE)

        for m in re_href.finditer(html):

            href = m.group(1)

            self.links.append(href)
