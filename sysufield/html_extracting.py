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
