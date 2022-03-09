#!/usr/bin/python
import re

for i in range(110):
    ret = re.match('[1-9]?[0-9]$', str(i))
    if ret:
        print('%s 匹配成功！' % str(i))
    else:
        print('%s 匹配失败！' % str(i))
