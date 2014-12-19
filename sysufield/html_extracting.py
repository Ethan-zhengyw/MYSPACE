#-*-encoding: utf-8-*-
import re

def find_jid_lt(data):
    """find the jsessionid in data

    This jsessionid will be use in get https://sso.sysu.edu.cn/cas/js/cas.js;jsessionid=AE150988B8BA701830907F6C074526B9

    :param data: ...<form id="fm1" class="fm-v clearfix" action="/cas/login;jsessionid=AE150988B8BA701830907F6C074526B9?service=http://ecampus.sysu.edu.cn/PersonalSpace/jsp/first.jsp" method="post">...<input type="hidden" name="lt" value="LT-746545-eXU4n0eKaGgcq4x7lVSWrD9VpRa1IR" />...
    :returns: `jid` - in this example is AE150988B8BA701830907F6C074526B9

    """

    regexp_jid = 'cas.js;jsessionid=(.*?)"'
    jid = re.search(regexp_jid, data).group(1)

    regexp_lt = 'name="lt"\ value="(.*?)"'
    lt = re.search(regexp_lt, data).group(1)

    return jid, lt
