#-*-encoding: utf-8-*-
import urllib2
import cookielib
import gzip
from StringIO import StringIO

import post_module as pm
import html_extracting as he

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

def get_opener():
    
    url = 'https://sso.sysu.edu.cn/cas/login?'\
            'service=http://ecampus.sysu.edu.cn/PersonalSpace/jsp/first.jsp'
    req = pm.req_easy_req(url)
    result = opener.open(req).read()

    jid, lt = he.find_jid_lt(result)
    print jid, lt

    #使用获得的jsessionid进行和CA握手之类的操作
    url_2 = 'https://sso.sysu.edu.cn/cas/js/cas.js;jsessionid=' + jid
    req_2 = pm.req_easy_req(url_2)
    opener.open(req_2)

    #握手后可以进行NetID登陆
    req_3 = pm.req_login(jid, lt, 'zheng', 'Trps', cookie)
    result_3 = opener.open(req_3)

    print result_3.read()
    print result_3.info()
    print result_3.url
    print cookie



def get_cjyl(page=1):
    """场地一览

    :param page: a page contain 10 records
    :returns:
        `counts` - the number of total records
        `result` - the content of a page with 10 records

    """

get_opener()
