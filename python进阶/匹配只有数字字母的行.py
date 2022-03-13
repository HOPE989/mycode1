#!/usr/bin/python
import re

text1 = """123abc
aBc123
------
******
a1c2b3"""
str1 = re.split('\n', text1)
for i in str1:
    ret = re.search('([a-zA-Z]|0-9)+', i)
    if ret:
        print(i)
