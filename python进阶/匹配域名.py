#!/usr/bin/python
import re

web = 'http://www.yahoo.edu'

ret = re.findall(r'www\.[\w]+\.(?:com|edu|net)', web)
print(ret)
