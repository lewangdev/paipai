#encoding=utf-8
import os
import sys
padding = lambda i : "00"[len(str(i)):] + str(i)
year = sys.argv[1]
cmd = "curl 'http://bidwiz.duapp.com/bwCheckController.do?getBidHistoricalData' -H 'Pragma: no-cache' -H 'Origin: http://bidwiz.duapp.com' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: no-cache' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: BAEID=4724761A7C3840DD497963D92D9FC2CB:FG=1; JSESSIONID=B2F42E15B2025405D69F3E1A731961C5' -H 'Connection: keep-alive' -H 'X-FirePHP-Version: 0.0.6' -H 'Referer: http://bidwiz.duapp.com/webpage/bidwiz/analyseData.jsp' --data 'bidMonth=%s%s&page=1&rows=500' --compressed -o %s%s.json"
for i in xrange(10, 11):
    j = i + 1
    c=  cmd % (year,padding(j), year,padding(j))
    print c
    os.system(c)
