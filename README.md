#Python PoC
项目概述：造轮子的第一步，一款Python 3下的Web安全检测PoC&&EXP模板的编写及整理，以及国内公开PoC代码分析

----
###　　　　　　　　　　　　Coder:crown prince
###　　　　　　　　　 E-mail:crownprince@windpunish.net

===========================
##前言：

编写这款程序的最终目标，是希望实现一款python 3下的Web安全检测PoC&&EXP框架，目前已经推出的、知名的、相类似的框架，是仅在py 2.7下的tangscan及Pocsuite，目前笔者所完成的，是创造这个轮子的第一步，python 3下的一款PoC&&EXP模板

###这套模板实现了什么？
1.在阅读了几乎所有乌云上的、知名博客上的公开PoC及EXP代码后，笔者不禁发现，尽管PoC的编写或许有大同小异之处，但在这些不同的代码中存在着许多相同，相同的代码中存在着许多不同，而往往，正是在这样每一个细节上，能够为茫然中的coder带来帮助，为coder所编的代码，带来一个质的改进，因此笔者将这些PoC中的典型案例做了分析整理，集中到了：http://www.windpunish.net/poc/exp.html

    对于SQL注入漏洞，根据漏洞出处，注入类型，注入语句，PoC中的亮点和关键等进行了分类，
    对于其他漏洞，比如XXE，撞库攻击，进行了分类和总结，同时，也在阅读代码过程中，尽力找到
    最合适的编写PoC的方式，比如，什么样的回显会更加清晰？SQL盲注时，记录时间是否会更好？等等

2.在完成了对PoC的代码分析后，笔者进行了此款模板的编写，目前，模板已经支持：

    任意文件下载漏洞 PoC  (Arbitrary_File_Download.py)
    Blind XXE漏洞 PoC  (Blind_XXE.py)
    XXE DoS（拒绝服务）漏洞 PoC  (XXE_DoS_Exp.py)
    XXE DoS（拒绝服务）漏洞 EXP  (XXE_DoS_PoC.py)
    POST XSS漏洞 PoC （python及html)  （Post_XSS.html，Post_XSS.py)
    任意文件上传漏洞 PoC (File_Upload.py)
    get类型 sql注入 PoC  (get_sql_injection_PoC.py)
    post类型 sql注入 PoC  (post_sql_injection_PoC.py)
    cookie类型 mysql数据库 time based盲注 EXP  (cookie_mysql_time-based-blind.py)
    get类型 mysql数据库 time based盲注 EXP 风格一   (get_mysql_time-based-blind.py)
    get类型 mysql数据库 time based盲注 EXP 风格二   (get_mysql_time-based-blind-2.py)
    post类型 mysql数据库 time based盲注 EXP  (post_mysql_time-based-blind.py)
同时，编写的模板，为了以后实现框架，能拥有更好的兼容性，笔者尽力做了详尽的注释, 并保证代码风格基本相同

###为什么要编写这套模板？为什么要选择Python 3？
在许多漏洞平台上，论坛上，附PoC脚本的漏洞往往都会引发关注，这证明，PoC这一领域有许多学习者，实践者，而笔者编写这套模板即希望,帮助学习PoC及EXP编写的小伙伴，更方便、高效、有效的的学习，帮助已经可以编写POC及EXP的小伙伴，更好的解决编写中的困难
选择python 3的原因：目前python 2.7下已经有一些不错的PoC框架了，而python 3 作为一个冉冉升起的新时代，笔者希望，这套模板，以及造轮子的第二步，及整套框架的实现，能为python 3下未来更多的
Web安全工作者、学习者、白帽子提供帮助，安全需要每一个安全人士的努力，而每一点的努力，都会是值得的

###关于重复做轮子：
笔者并不反对重复造轮子，一辆宝马有4个轮子，一辆火车更是有一大堆轮子，而少了任何一个都不行，所以，笔者认为，优秀的轮子，就是好轮子 :)
如何将轮子造的完美，才是工匠最应该考虑的

##项目介绍：

###PoC及EXP整理分析，采用表格形式呈现<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/%E5%85%AC%E5%BC%80PoC%E5%8F%8AEXP%E5%88%86%E6%9E%90.png)  
<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/%E5%85%AC%E5%BC%80PoC%E5%8F%8AEXP%E5%88%86%E6%9E%90-2.png) 

###GET型mysql注入核心代码及使用样例<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/get%E5%9E%8Bsql%E6%B3%A8%E5%85%A5%E6%A0%B7%E4%BE%8B.png)  
<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/get_mysql_time-based-blind.png)  

###任意文件下载漏洞核心代码及使用样例<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%BC%8F%E6%B4%9E%E4%B8%BE%E4%BE%8B.png) 
<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/Arbitrary_File_Download%281%29.png) 
<br>
![](https://github.com/crown-prince/Python_PoC/blob/master/Arbitrary_File_Download%282%29.png) 


##意见与建议：

----

欢迎大家在使用过程中提出各种宝贵的意见和建议，以及各种bug，不胜感激

反馈邮箱crownprince@windpunish.net

鸣谢：感谢团队小伙伴苍冥在项目开发中提供的支持、建议和帮助
