import urllib.request as urlreq
import urllib.error
import os
import sys
import requests
from tqdm import tqdm
import zipfile

def install(u):
    f = u.split(",")
    f[0] = f[0].split("/")[2]

    t = requests.get(
        "https://api.gamebanana.com/Core/Item/Data?itemtype=Mod&itemid={0}&fields=name".format(f[2])).json()

    yn = str(input("Do you want to install {0}?".format(t[0]) + " (Y/N) "))
    if yn.lower().startswith("y"):
        file = f[0] + ".zip"
        modsPatch = os.path.abspath(os.path.dirname(os.getcwd() + "/Mods/"))
        cacheFile = modsPatch + os.path.sep + "cache" + os.path.sep + file
        f = requests.get("https://gamebanana.com/dl/" +
                 f[0], stream=True)
        if not os.path.exists(modsPatch):
            os.mkdir("Mods")
        if not os.path.exists(modsPatch + os.path.sep + "cache"):
            os.mkdir("Mods/cache")
        with open(modsPatch + os.path.sep + "cache" + os.path.sep + file, "wb") as handle:
            for data in tqdm(f.iter_content(), desc="Downloading "):
                handle.write(data)
            handle.close()
        with zipfile.ZipFile(cacheFile) as zf:
            extPatch = modsPatch + os.path.sep + t[0]
            if not os.path.exists(extPatch):
                os.mkdir("Mods/" + t[0])
            for member in tqdm(zf.infolist(), desc="Extracting "):
                try:
                    zf.extract(member, extPatch)
                except zipfile.error:
                    pass
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