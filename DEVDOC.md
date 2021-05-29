# Developper's Documentation

## Protocol reference

An FMI protocol URL start with `fmi://`. There are 3 fields: `[URL_TO_ARCHIVE]`, `[MOD_TYPE]` and `[MOD_ID]`. A typical FMI protocol URL look like this:

`fmi://https://gamebanana.com/mmdl/578921,Mod,289280`

## Build (for Windows)
You need Python and Pip for build!

```sh
# Install dependancies
pip3 install -r requirements.txt
# Compile main codes files
pyinstaller --noconfirm --onefile --windowed --name "fmi" main.py
pyinstaller --noconfirm --onefile registerProtocol.py
pyinstaller --noconfirm --onefile removeProtocol.py
```