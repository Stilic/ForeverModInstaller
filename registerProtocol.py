import winreg
import os

proto = "fmi"

key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, proto)
winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
winreg.CloseKey(key)

key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                       proto + "\shell\open\command")
if os.path.exists(os.getcwd() + os.path.sep + "fmi.exe"):
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ,
                      '"{0}" "%1"'.format(os.getcwd() + os.path.sep + "fmi.exe"))
else:
    print("'fmi.exe' file not found! Please add it or rename fmi excutable into 'fmi.exe'!")

winreg.CloseKey(key)