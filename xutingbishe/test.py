#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
'''
	遍历目录，将目录中所有文件进行提取关键词，并把关键词保存到指定文件
'''

def readFile(filename):
    f = open(filename, "r",encoding= 'utf-8')
    content = f.readlines()
    # print(content)
    f.close()
    return ''.join(content)

def findWordsByTag(str, tag):
    xx = "(\\b[\u4e00-\u9fa5|\S]+)/" + tag
    results = re.findall(xx, str)
    return results

def getCounnt(strList):
    wordcnt = {}
    for i in strList:
        if i in wordcnt:
            wordcnt[i] += 1
        else:
            wordcnt[i] = 1
    return wordcnt

def writeFile(filename, content):
    f = open(filename, "a")
    f.write(content)
    f.close()

def writeCnttoFile(filename, wordcntSorted, resultfile):
    str = "{" + filename + ":{"
    k = 0
    for i in wordcntSorted:
        if k < 2:
            k = k + 1
            str += "%s:%d,"%i
        elif k == 3:
            str += "%s:%d"%i
            break
    str += "}}\n"

    print(str)
    writeFile(resultfile, str)

def doFile(filename, tag, resultfile):
    str = readFile(filename)
    list = findWordsByTag(str, tag)
    wordcnt = getCounnt(list)
    wordcntSorted = sorted(wordcnt.items(), key=lambda wordcnt:wordcnt[1], reverse=True)
    writeCnttoFile(filename, wordcntSorted, resultfile)

def dfsFolder(rootDir, tag, resultfile):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        #for d in dirs:
        #   print(os.path.join(root, d))
        #  writeFile("c:\\test.txt", os.path.join(root, d) + "\n")
        for f in files:
            #print(os.path.join(root, f))
            #writeFile("c:\\test.txt", os.path.join(root, f) + "\n")
            file = os.path.join(root, f)
            doFile(file, tag, resultfile)





if __name__ == "__main__":
    dfsFolder("C:\\200000\\", "b", "c:\\test.txt")





