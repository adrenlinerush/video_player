#!/usr/bin/env python
import os
import subprocess
from simple_term_menu import TerminalMenu

videos_dir="/mnt/Videos"
current_dir=videos_dir

subprocess.run(["clear"])

while True:
    selection=[]
    add_parent=True
    for d in os.listdir(current_dir):
        if (current_dir != videos_dir) and add_parent:
            selection.append("..")
            add_parent = False
        selection.append(d)

    selection_menu = TerminalMenu(selection, title="Video Player\n\nPlease Select a Video to Play.")
    index = selection_menu.show()

    if selection[index] == "..":
        path_ary=current_dir.split("/")
        path_ary.pop()
        current_dir= "/".join(path_ary)
    elif os.path.isfile(current_dir+"/"+selection[index]):
        subprocess.run(["/usr/bin/qeglfsvideoplayer", current_dir+"/"+selection[index]])
        subprocess.run(["clear"])
        current_dir=videos_dir
    else:
        current_dir=current_dir+"/"+selection[index]
