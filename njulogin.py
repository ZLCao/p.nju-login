#!/usr/bin/python2

import urllib
import urllib2

login_info_raw = {'username': 'stu id', 'password': '******'}
login_info= urllib.urlencode(login_info_raw)

login_url  = 'http://p.nju.edu.cn/portal_io/login'
logout_url = 'http://p.nju.edu.cn/portal_io/logout'

while 1:

    log = raw_input('login[i] or logout[o]: ')

    if log in ['login', 'i', 'I' ]:
        req = urllib2.Request(url = login_url, data = login_info)
        break
    elif log in ['logout', 'o', 'O' ]:
        req = urllib2.Request(url = logout_url, data = '')
        break
    else:
        print 'Invalid input! Please input again!'

res_data = urllib2.urlopen(req)
res = res_data.read()
reply_msg = eval(res)['reply_msg']
print reply_msg
