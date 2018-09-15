#coding:UTF-8
import urllib2
from bs4 import BeautifulSoup as bs
import time

class spider():
    def __init__(self,id):
        self.id=id
        self.ans=""

    def getInfo(self):#输入题目html代码
        print u"    [INFO]正在解析网页源代码"
        print self.code
        #查看网页源代码发现题目内容的在某个DIV标签下，用BtF将其转出吗
        # soup=bs(self.code,features ="lxml")#创建soup对象,第二个参数是摆脱警告
        # print u"    [INFO]正在查找相关目标"
        # print soup.find_all("div",class_="am-u-md-8 lg-right")
        #由于特殊结构，soup暂时无法使用，这里使用栈来解决
        ind=self.code.find('<div class="lg-article am-g">')
        if ind==-1:
            print u"    [Erro]爬取失败"
        else:
            more=self.code.find("</div>",ind)+6
            #不再内嵌div，所以可以搞定
            ans=self.code[ind:more]
            self.ans+="\n\n\n"+self.id+":\n"+ans

    def getHtml(self):#输入题目ID返回html代码
        print u"    [INFO]正在获取网页源代码"
        url="http://www.luogu.org/problemnew/show/P"+self.id
        page=urllib2.urlopen(url)
        html=page.read()
        self.code=html

    def __str__():
        return self.ans

#创建对象
print u"输入需要提取的题目编号，不带'P',如需批量获取，请用半角逗号隔开",
for i in raw_input().split(","):
    print u"[RUN]正在爬取"+i
    sp=spider(i)
    sp.getHtml()
    sp.getInfo()
print u"[INFO]正在保存文件"
f=open("ans.html","w")
f.write(sp)
f.close()
print u"[INFO]结果文件保存在asn.html"
import os
os.system("ans.html")


