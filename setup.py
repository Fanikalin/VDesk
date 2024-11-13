from zipfile import ZipFile
import os
import sys

GIT_LINK = "https://github.com/Fanikalin/VDesk"

IS_PLATFORM_WIN = sys.platform.lower().startswith("win")

CMD_PYTHON = "python" if IS_PLATFORM_WIN else "python3"


os.system(CMD_PYTHON + " -m venv .venv")
CMD_PYTHON = ".\\.venv\\Scripts\\python.exe" if IS_PLATFORM_WIN else "./.venv/bin/python"

if os.path.exists("VDesk-main.zip"):
    os.remove("VDesk-main.zip")

os.system(CMD_PYTHON + " -m pip install wget")
os.system(CMD_PYTHON + " -m wget "+GIT_LINK+"/archive/main.zip")


archive = ZipFile("VDesk-main.zip", "r")

for file in archive.infolist():
    name = os.path.split(file.filename.removeprefix(".").removeprefix("/").removeprefix("\\").removeprefix("VDesk-main"))
    
    if name[1] == "":
        continue

    os.makedirs("."+name[0], exist_ok=True)

    try:
        open("."+os.path.join(name[0], name[1]), "wb").write(archive.read(file))
    except PermissionError:
        pass

archive.close()

os.system(CMD_PYTHON + " -m pip install -r requirements.txt")

os.remove("VDesk-main.zip")