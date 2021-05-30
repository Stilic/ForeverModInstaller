import urllib.request as urlreq
import urllib.error
import os
import sys
import requests
from tqdm import tqdm
import zipfile
from glob import glob
import shutil


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
        extPatch = modsPatch + os.path.sep + t[0]
        with zipfile.ZipFile(cacheFile) as zf:
            if not os.path.exists(extPatch):
                os.mkdir("Mods/" + t[0])
            for member in tqdm(zf.infolist(), desc="Extracting "):
                try:
                    zf.extract(member, extPatch)
                except zipfile.error:
                    pass
        folders = []
        for fol in os.listdir(modsPatch + os.path.sep + t[0]):
            if os.path.isdir(modsPatch + os.path.sep + fol):
                folders.append(fol)
        if len(folders) == 1:
            for p in glob(modsPatch + t[0] + "/" + folders[0]):
                print(p)
                shutil.move(p, t[0])
            mps = "./Mods"
            shutil.move(mps + "/" + t[0] + "/" + t[0], "./")
            shutil.rmtree(mps + "/" + t[0])
            shutil.move(t[0], mps)
        if os.path.isfile(cacheFile):
            os.remove(cacheFile)
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
