from tkinter import Button
import handler
from guizero import *
import urllib.request
from pathlib import Path
import os
from zipfile import ZipFile

def getModsPath():
    return os.path.abspath(os.path.dirname(os.getcwd() + "/Mods/"))


def installmod():
    f = handler.debug.testUrl(url.value)
    if not os.path.exists("Mods/cache"):
        os.makedirs("Mods/cache")
    file = f[0] + ".zip"
    urllib.request.urlretrieve("https://gamebanana.com/dl/" + f[0], os.path.abspath(
        getModsPath() + os.path.sep + "cache" + os.path.sep + file))
    with ZipFile(getModsPath() + os.path.sep + "cache" + os.path.sep + file, 'r') as zip:
        zip.extractall(getModsPath())
    if os.path.exists("Mods/cache/" + file):
        os.remove(getModsPath() + os.path.sep + "cache" + os.path.sep + file)


app = App(title="Forever Mod Installer")
Text(app, text="Install via fmi protocol")
url = TextBox(app, width=25)
PushButton(app, text="Install", command=installmod)

app.display()
