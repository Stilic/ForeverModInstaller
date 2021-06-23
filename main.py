import urllib.request as urlreq
import urllib.error
import os
import sys
import mimetypes
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(os.path.dirname(sys.executable))
from download import download
import sys
import requests
from glob import glob
import shutil
from pyunpack import Archive


def install(u):
    f = u.split(",")
    f[0] = f[0].split("/")[2]

    t = requests.get(
        "https://api.gamebanana.com/Core/Item/Data?itemtype=Mod&itemid={0}&fields=name".format(f[2])).json()

    yn = str(input("Do you want to install {0}?".format(t[0]) + " (Y/N) "))
    if yn.lower().startswith("y"):
        finalURL = "https://gamebanana.com/dl/" + f[0]
        file = t[0] + mimetypes.guess_extension(
            requests.get(finalURL).headers.get("Content-Type"))
        modsPatch = os.path.abspath(os.path.dirname(os.getcwd() + "/Mods/"))
        cachePath = modsPatch + os.path.sep + "cache" + os.path.sep
        cacheFile = cachePath + file
        extPatch = modsPatch + os.path.sep + t[0]
        download(finalURL, cacheFile, replace=True)
        if not os.path.isdir(extPatch):
            os.mkdir(extPatch)
        else:
            shutil.rmtree(extPatch)
            os.mkdir(extPatch)
        Archive(cacheFile).extractall(extPatch)
        folders = []
        for fol in os.listdir(modsPatch + os.path.sep + t[0]):
            if os.path.isdir(modsPatch + os.path.sep + fol):
                folders.append(fol)
        if len(folders) == 1 and folders[0] != "Data":
            for p in glob(modsPatch + t[0] + "/" + folders[0]):
                print(p)
                shutil.move(p, t[0])
            mps = "./Mods"
            shutil.move(mps + "/" + t[0] + "/" + t[0], "./")
            shutil.rmtree(mps + "/" + t[0])
            shutil.move(t[0], mps)
        if os.path.isfile(cacheFile):
            shutil.rmtree(cachePath)
        input("{0} installed! Press Enter for exit...".format(t[0]))
    else:
        print("bye")


class handler(urlreq.BaseHandler):
    def fmi_open(self, req):
        fullUrl = req.get_full_url()
        url = "".join(fullUrl.split("://")[1:])
        install(url)


opener = urlreq.build_opener(handler())
urlreq.install_opener(opener)
try:
    urlreq.urlopen(sys.argv[1])
except urllib.error.URLError:
    pass
