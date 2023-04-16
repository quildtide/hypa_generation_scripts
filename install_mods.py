import shutil
import os
import json

from pa_directory import mods_path

def install_mod(mod_path):
    install_path = os.path.join(mods_path, mod_path)
    if os.path.isdir(install_path):
        shutil.rmtree(install_path)

    shutil.copytree(mod_path, install_path, dirs_exist_ok=True)

    modinfo_path = os.path.join(install_path, "modinfo.json")
    with open(modinfo_path, 'r') as modinfo_file:
        info = json.load(modinfo_file)
        info["identifier"] = info["identifier"] + "-dev"
    
    with open(modinfo_path, 'w') as modinfo_file:
        json.dump(info, modinfo_file)

install_mod("hypa")