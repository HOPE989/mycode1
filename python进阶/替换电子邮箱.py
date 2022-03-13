#!/usr/bin/python
import re

mails = '123abc@163.com\n' \
        '123abc@qq.com\n' \
        '123abc@gmail.com\n' \
        '123abc@126.com\n' \
        '123abc@111.com\n' \
        '123abc@222.com\n'
ret_s = re.sub(r'[a-zA-Z0-9_]{4,20}@[a-zA-Z0-9]+\.com', r'836495061@qq.com', mails)
print(ret_s)
