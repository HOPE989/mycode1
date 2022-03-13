#!/usr/bin/python
import re

str1 = 'abc123def'
ret = re.match('[a-zA-Z]+', str1)
print(ret.group())
