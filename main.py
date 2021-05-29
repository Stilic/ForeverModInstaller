from guizero import *
import urllib.request as urlreq
import urllib.parse as urlparse
from urllib.parse import parse_qs
from io import StringIO as strio
from pathlib import Path
import os
import requests
from zipfile import ZipFile
import gbapi
gb = gbapi.Client()

f = []

app = App(title="Forever Mod Installer", visible=False)


def getModsPath():
    return os.path.abspath(os.path.dirname(os.getcwd() + "/Mods/"))


def installmod(f):
    t = requests.get(
        "https://api.gamebanana.com/Core/Item/Data?itemtype=Mod&itemid={0}&fields=name".format(f[0])).json

    yn = yesno("Forever Mod Installer",
               "Do you want to install {0} ?".format(t[0]))
    if yn == True:
        if not os.path.exists("Mods/cache"):
            os.makedirs("Mods/cache")
        file = f[0] + ".zip"
        urlreq.urlretrieve("https://gamebanana.com/dl/" + f[0], os.path.abspath(
            getModsPath() + os.path.sep + "cache" + os.path.sep + file))
        with ZipFile(getModsPath() + os.path.sep + "cache" + os.path.sep + file, 'r') as zip:
            zip.extractall(getModsPath())
        if os.path.exists("Mods/cache/" + file):
            os.remove(getModsPath() + os.path.sep +
                      "cache" + os.path.sep + file)


class handler(urlreq.BaseHandler):
    def fmi_open(self, req):
        fullUrl = req.get_full_url()
        f = "".join(fullUrl.split("://")[1:])
        f = f.split(",")
        ft = f[0].split("/")
        f[0] = ft[len(ft) - 1]
        installMod(f)


opener = urlreq.build_opener(handler())
urlreq.install_opener(opener)

app.display()
