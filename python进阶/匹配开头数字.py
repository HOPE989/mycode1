#!/usr/bin/python
import re

str1 = '123abc456'
ret = re.match('[0-9]+', str1)
print(ret.group())
