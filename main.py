#coding:UTF-8
import urllib2
from bs4 import BeautifulSoup as bs
import time

# import urllib.request
 
#定义保存函数
def saveFile(data):
    path = "E:\\projects\\Spider\\02_douban.out"
    f = open(path,'wb')
    f.write(data)
    f.close()
 



class spider():
    def __init__(self,id):
        self.id=id
        self.ans=""

    def getInfo(self):#输入题目html代码
        print u"    [INFO]正在解析网页源代码"
        # print '<div class="lg-article am-g">' in self.code
        #查看网页源代码发现题目内容的在某个DIV标签下，用BtF将其转出吗
        soup=bs(self.code,features ="lxml")#创建soup对象,第二个参数是摆脱警告
        print u"    [INFO]正在查找相关目标"
        print soup.find_all("div",class_="am-topbar-form am-topbar-right am-form-inline lg-hide")
        # ind=self.code.find('<div class="lg-article am-g">')
        # if ind==-1:
        #     print u"    [Erro]解析失败"
        # else:
        #     more=self.code.find("</div>",ind)+6
        #     #不再内嵌div，所以可以搞定
        #     ans=self.code[ind:more]
        #     self.ans+="\n\n\n"+self.id+":\n"+ans

    def getHtml(self):#输入题目ID返回html代码
        print u"    [INFO]正在获取网页源代码"
        url="http://www.luogu.org/problemnew/show/P"+self.id
        import urllib2
        # url="http://pythontab.com"
        req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept':'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding':'gzip',
        'Connection':'close',
        'Referer':None #伪装成浏览器爬取 注意如果依然不能抓取的话，这里可以设置抓取网站的host
        }
        req_timeout = 5
        req = urllib2.Request(url,None,req_header)
        resp = urllib2.urlopen(req,None,req_timeout)
        html = resp.read()
        self.code=html

    def __str__(self):
        return self.code

#创建对象
print u"输入需要提取的题目编号，不带'P',如需批量获取，请用半角逗号隔开",
for i in raw_input().split(","):
    print u"[RUN]正在爬取"+i
    sp=spider(i)
    sp.getHtml()
    sp.getInfo()
print u"[INFO]正在保存文件"
f=open("ans.html","w")
f.write(sp.__str__())
f.close()
print u"[INFO]结果文件保存在ans.html"
import os
os.system("ans.html")


