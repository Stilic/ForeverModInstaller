import urllib.request as urlreq
from io import StringIO as strio
import sys
from install import install

class handler(urlreq.BaseHandler):
    def fmi_open(self, req):
        fullUrl = req.get_full_url()
        url = "".join(fullUrl.split("://")[1:])
        install(url)

opener = urlreq.build_opener(handler())
urlreq.install_opener(opener)

urlreq.urlopen(sys.argv[1])