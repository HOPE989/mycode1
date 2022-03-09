#!/usr/bin/python
import re

ret = re.match('[hb].t', 'bat')
print(ret.group())
ret = re.match('[hb].t', 'bit')
print(ret.group())
ret = re.match('[hb].t', 'but')
print(ret.group())
ret = re.match('[hb].t', 'hat')
print(ret.group())
ret = re.match('[hb].t', 'hit')
print(ret.group())
ret = re.match('[hb].t', 'hut')
print(ret.group())
