#-*-encoding: utf-8-*-
import urllib2
import cookielib
import StringIO, gzip

import post_module as pm
import html_extracting as he

def test_result(result):
    if result.info().get('Content-Encoding') == 'gzip':
        compressedstream = StringIO.StringIO(result.read())
        gziper = gzip.GzipFile(fileobj = compressedstream)
        print gziper.read()
    else:
        print result.read()
    print result.getcode()
    print result.info()
    print result.geturl()


class Field:

    def __init__(self, username, password):

        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.login(username, password)

    def login(self, username, password):

        self.opener.open(pm.simple_req('http://ecampus.sysu.edu.cn/zsuyy/login_normal.jsp'))
        self.opener.open(pm.login_req(username, password))

    def get_userinfo(self):

        req = pm.simple_req('http://ecampus.sysu.edu.cn/zsuyy/application/desktop.jsp')
        html = self.opener.open(req).read().decode('gbk')
        
        return he.find_userinfo(html)





zyw = Field('12330423', '08236135')
userinfo = zyw.get_userinfo()
print userinfo
