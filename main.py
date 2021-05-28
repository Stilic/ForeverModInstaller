import handler
from guizero import *

def update_text():
    label2.value = handler.debug.testUrl(name.value)

app = App(title="Forever Mod Installer")
label = Text(app, text="Test URL")
name = TextBox(app)
button = PushButton(app, text="Test", command=update_text)
label2 = Text(app)

app.display()