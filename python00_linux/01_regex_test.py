# -*- coding: UTF-8 -*-
import re

str = "abc 中文 haha"

temp = str.decode('utf8')

xx = u"([/u4e00-/u9fa5]+)"

results = re.findall(xx, temp)

for result in results :
    print result