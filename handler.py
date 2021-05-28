import urllib.request as urlreq
import urllib.parse as urlparse
from urllib.parse import parse_qs
from io import StringIO as strio
class PyProtoHandler(urlreq.BaseHandler):
    def fmi_open(self, req):
        fullUrl = req.get_full_url()
        f = "".join(fullUrl.split("://")[1:])
        return f.split(",")

opener = urlreq.build_opener(PyProtoHandler())
urlreq.install_opener(opener)

class debug:
    def testUrl(url):
        return urlreq.urlopen(url)