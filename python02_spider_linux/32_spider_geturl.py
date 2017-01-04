#-*- coding: utf-8 -*-
import re
import urllib
import threading

def getWebPage(url):
    wp = urllib.urlopen(url)
    content = wp.read()
    return content

def analysisPage(content, urllist, urlset):
    strlist = re.split('\"',content)
    geturlset = set([])
    for str in strlist:
        if re.match('http://www.cnblogs.com/(/|\w)+', str):
            geturlset.add(str + '\n')

    setlock.acquire()
    geturlset = geturlset - urlset
    setlock.release()

    listlock.acquire()
    for url in list(geturlset):
        urllist.append(url)
    listlock.release()

class MyThread(threading.Thread):
    def __init__(self, urllist, urlset):
        threading.Thread.__init__(self)
        self.urllist = urllist
        self.urlset = urlset

    def run(self):
        while True:
            listlock.acquire()
            if self.urllist:
                url = self.urllist.pop(0)
                listlock.release()
            else:
                listlock.release()
                break

            setlock.acquire()
            if len(self.urlset) >= 50:
                setlock.release()
                break
            else:
                if url in self.urlset:
                    setlock.release()
                    continue
                else:
                    self.urlset.add(url)
                    setlock.release()
                    content = getWebPage(url)
                    analysisPage(content, self.urllist, self.urlset)

listlock = threading.RLock()
setlock = threading.RLock()

if __name__ == '__main__':
    starturl = 'http://www.cnblogs.com/\n'
    content = getWebPage(starturl)
    #urlset存放已访问过的网页url
    #urllist存放待访问的网页url
    urlset = set([starturl])
    urllist = []
    analysisPage(content, urllist, urlset)    
    tlist = []
    for i in range(4):
        t = MyThread(urllist, urlset)
        t.start()
        tlist.append(t)
    for t in tlist:
        t.join()
    f = open('url.txt', 'w')
    f.writelines(list(urlset))
    f.close()
