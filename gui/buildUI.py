import os
from os.path import isfile, join
from os import listdir

cwd = os.getcwd() + "\\"

ui_files = [f for f in listdir("ui\\") if isfile(join("ui\\", f))]

ui_py = {x.replace('.ui', '.py') for x in ui_files}

if not os.path.exists("compiledUI"):
    os.mkdir("compiledUI")
    
for ui, uipy in zip(ui_files, ui_py):
    os.system("pyuic5 " + cwd + "ui\\" + ui + " -o" + " compiledUI\\" + uipy)

