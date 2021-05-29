import urllib.request as urlreq
import os
import requests
from zipfile import ZipFile
import sys
import aiohttp
session = aiohttp.ClientSession()
session.close()


def getModsPath():
    return os.path.abspath(os.path.dirname(os.getcwd() + "/Mods/"))


fullUrl = sys.argv[1]
f = "".join(fullUrl.split("://")[1:])
f = f.split(",")
ft = f[0].split("/")
f[0] = ft[len(ft) - 1]

t = requests.get(
    "https://api.gamebanana.com/Core/Item/Data?itemtype=Mod&itemid={0}&fields=name".format(f[0])).json

yn = str(input("Do you want to install {0} ?".format(t()[0]) + "(Y/N) "))

if yn == "y" or "Y":
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
