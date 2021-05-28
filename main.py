import handler
from guizero import *

def update_text():
    f = handler.debug.testUrl(name.value)
    label2.value = "url archive: {0}, mod type: {1}, mod id: {2}".format(f[0], f[1], f[2])

app = App(title="Forever Mod Installer")
label = Text(app, text="Test URL")
name = TextBox(app)
button = PushButton(app, text="Test", command=update_text)
label2 = Text(app)

app.display()