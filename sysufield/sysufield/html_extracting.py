#-*-encoding: utf-8-*-
"""HTML content processing

This file is the module to processing html content, using regular expression module to match the target content and return them to function in api.

"""
import re


def find_userinfo(html):

    regexp = '(?<=article_subhead1">)(.*)(?=</span>)'
    result = re.findall(regexp, html)
    
    userinfo = {
        'xh': result[0],
        'xm': result[1],
        'xy': result[2]
    }

    return userinfo


def find_identified_url(html):

    regexp = '(?<=deURIComponent\(")(.*?)(?="\))'
    result = re.search(regexp, html)

    url = 'http://ecampus.sysu.edu.cn/repp/redirect?identity='\
            + result.group(0) + '&url=/repp/c/hc/applies'

    return url


def find_ts_url(html, kind='applies', page=1):

    regexp = '(?<=_ts=)(.*)(?=\',)'
    result = re.search(regexp, html)

    url = 'http://ecampus.sysu.edu.cn/repp/c/hc/' + kind + '?'
    url = url + 'page=' + str(page) + '&' if kind == "applies" else url
    url = url + '_ts=' + result.group(0)
    
    return url


def find_field_detail(html, kind='applies'):

    if kind == "applies":
        result = find_applications(html)
    else:
        result = find_schedule(html)

    return result


def find_applications(html):

    print html


def find_schedule(html):

    print
