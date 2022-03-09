#!/usr/bin/python
# xxxx@163.com
import re

emails = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in emails:
    ret = re.match('[\w]{4,20}@163\.com$', email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合规定" % email)
