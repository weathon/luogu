import requests
j=input("PID>")
header={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
#不构造浏览器UA会导致404
r = requests.get('https://www.luogu.org/problemnew/show/P'+str(j),headers=header)
try:
    print(r.text)
    begin=r.text.find('<div class="lg-article am-g">')
    end=r.text.find("<div class='lg-article-sub am-g' id=\"sub\"></div>",begin)
    html=r.text[begin:end]
    with open("ans.html","w") as f:
        f.write(html)
    print("Finish! HTML answer is in ans.html!")
except:
    print("Error")