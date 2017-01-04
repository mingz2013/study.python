import re

m = re.search('[0-9]','abcd4ef')
print(m.group(0))
#n = re.match('[0-9]','abcde4f')
#print(n.group(0))

str = re.sub('[0-9]','123','abcde4f')
print(str.group(0))


