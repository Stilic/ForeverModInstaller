import urllib
import os
import requests
from download import download


def install(u):
    modsPath = os.path.abspath(os.path.dirname(os.getcwd() + "/Mods/"))

    f = u.split(",")
    f[0] = f[0].split("/")[2]

    t = requests.get(
        "https://api.gamebanana.com/Core/Item/Data?itemtype=Mod&itemid={0}&fields=name".format(f[2])).json()

    yn = str(input("Do you want to install {0}?".format(t[0]) + " (Y/N) "))
    if yn == "y" or "Y":
        file = f[0] + ".zip"
        download("https://gamebanana.com/dl/" +
                 f[0], modsPath + "/" + t[0], kind="zip", replace=True)
