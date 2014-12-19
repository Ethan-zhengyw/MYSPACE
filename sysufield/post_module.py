#-*-encoding: utf-8-*-
"""Main Request object

This file contains some definition of Request object to be used in api to get the content of certain website page

"""
import urllib
import urllib2

# Request header pretend to be browser
header = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64;\
            Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;\
            Media Center PC 6.0; .NET4.0C; InfoPath.3; .NET4.0E; Shuame)"
}

def req_easy_req(address):
    """Create a simple request

    This function provide a simple way to create a request with browser header.

    :param address: The url to request
    :returns: `req` - a request object with a browser header

    """
    req = urllib2.Request(
        url = address,
        headers = header
    )

    return req

def req_login(jid, lt, username, password, cookie):

    #url_ = 'https://sso.sysu.edu.cn/cas/login;jsessionid=' + jid + '?'\
    #        'service=http://ecampus.sysu.edu.cn/PersonalSpace/jsp/first.jsp'

    url_ = 'https://sso.sysu.edu.cn/cas/login?'\
            'service=http://ecampus.sysu.edu.cn/PersonalSpace/jsp/first.jsp'

    header_jid = [j.value for j in cookie]

    login_header = {
        'Host': 'sso.sysu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Referer': 'https://sso.sysu.edu.cn/cas/login;' + header_jid[0] + '?service=http://ecampus.sysu.edu.cn/PersonalSpace/jsp/first.jsp',
        'Cookie': 'JSESSIONID=' + header_jid[0],
        'Connection': 'keep-alive'
    }

    postdata = urllib.urlencode({
        'username': username,
        'password': password,
        'lt': lt,
        'execution': 'e1s1',
        '_eventid': 'submit',
        'code': '',
        'submit': '登陆'
    })

    print postdata
    print login_header
    req = urllib2.Request(
        url = url_,
        data = postdata,
        headers = header
    )

    return req
