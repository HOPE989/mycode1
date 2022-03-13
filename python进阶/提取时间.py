#!/usr/bin/python
import re

str1 = 'now is 2022/3/13 18:48, 现在是 2022年2月13日18时48分。\n' \
       'now is 2022/3/14 18:48, 现在是 2022年2月14日18时48分。\n' \
       'now is 2022/3/15 18:48, 现在是 2022年02月15日06时05分。\n'
ret_s = re.sub(r'年|月', r'/', str1)
ret_s = re.sub(r'日|分', r' ', ret_s)
ret_s = re.sub(r'时', r':', ret_s)
print(ret_s)
com = re.compile(r'[\d]{4}/[01]?[0-9]/[1-2]?[\d]\s[0-2]?[\d]:[0-5]?[\d]')
print(com.findall(ret_s))
