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

    def get_field_detail(self, kind='schedule', page=1):
        """ 查询场地的详情

        :param kind: `applies`表示场地申请情况，`schedule`表示场地占用情况即已经通过审批的申请，传入一个错误的值会返回场地的占用情况
        :param page: 此参数在kind=`applies`时才需要使用，一页有10条记录，而场地占用会直接将所有占用记录返回
        :returns: `result` - 一个包含多个字典的列表，每个字典是一条记录

        """
        identified_url = he.find_identified_url(
            self.opener.open(pm.simple_req(
                'http://ecampus.sysu.edu.cn/zsuoa/'\
                        'application/oa/hc/redirect.jsp?method=' + kind
            )).read()
        )
        ts_url = he.find_ts_url(
            self.opener.open(pm.simple_req(identified_url)).read(), kind, page
        )

        req = pm.simple_req(ts_url)
        html = self.opener.open(req).read().decode('gbk')

        result = he.find_field_detail(html, kind)






zyw = Field('12330423', '08236135')

userinfo = zyw.get_userinfo()

applies = zyw.get_field_detail('applies', 2)
#schedule = zyw.get_field_detail('schedule')

for key in userinfo:
    print key, userinfo[key]
print applies
#print schedule
