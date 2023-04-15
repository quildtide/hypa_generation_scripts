import shutil
import os

from pa_directory import mods_path

def install_mod(mod_path):
    install_path = os.path.join(mods_path, mod_path)
    if os.path.isdir(install_path):
        shutil.rmtree(install_path)

    shutil.copytree(mod_path, install_path, dirs_exist_ok=True)

install_mod("hypa")