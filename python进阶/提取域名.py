#!/usr/bin/python
import re

str1 = '''
http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
ret_s = re.sub(r'http://', '', str1)
ret_s = re.split('\n', ret_s)
for i in ret_s:
    ret = re.match('[^/]+', i)
    if ret:
        print(ret.group())
