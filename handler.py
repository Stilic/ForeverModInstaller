import urllib.request as urlreq
import urllib.parse as urlparse
from urllib.parse import parse_qs
from io import StringIO as strio


class handler(urlreq.BaseHandler):
    def fmi_open(self, req):
        fullUrl = req.get_full_url()
        f = "".join(fullUrl.split("://")[1:])
        f = f.split(",")
        ft = f[0].split("/")
        f[0] = ft[len(ft) - 1]
        return f


opener = urlreq.build_opener(handler())
urlreq.install_opener(opener)


class debug:
    def testUrl(url):
        return urlreq.urlopen(url)
