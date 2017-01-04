dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print dic[key]
print '************************'
print dic.keys()
print dic.values()
print dic.items()
del dic['tom']
print dic
dic.clear()
print dic
print '*******print(len(dic))**********'
print(len(dic))
