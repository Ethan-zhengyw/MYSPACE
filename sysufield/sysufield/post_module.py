#-*-encoding: utf-8-*-
"""Main Request object

This file contains some definition of Request object to be used in api to get the content of certain website page

"""
import urllib
import urllib2

# Request header
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1;'\
            'WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727;'\
            '.NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0;'\
            '.NET4.0C; InfoPath.3; .NET4.0E; Shuame)',
    #'Accept-Encoding': 'gzip'
}


def simple_req(address):
    """get a simple request object 

    :param address: the url to open
    :returns: `Request` - a Request object

    """

    req = urllib2.Request(
        url = address,
        headers = header
    )

    return req


def login_req(username, password):

    post_data = urllib.urlencode({
        'j_username': username,
        'j_password': password,
        'x': '0',
        'y': '0'
    })

    req = urllib2.Request(
        url = 'http://ecampus.sysu.edu.cn/zsuyy/login.do',
        data = post_data,
        headers = header
    )

    return req

