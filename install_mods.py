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
        if "dependencies" in info:
            if "com.pa.daedalus.hypa" in info["dependencies"]:
                info["dependencies"].remove("com.pa.daedalus.hypa")
                info["dependencies"].append("com.pa.daedalus.hypa-dev")
            elif "com.pa.daedalus.hypa_submod_legion" in info["dependencies"]:
                info["dependencies"].remove("com.pa.daedalus.hypa_submod_legion")
                info["dependencies"].append("com.pa.daedalus.hypa_submod_legion-dev")
    
    with open(modinfo_path, 'w') as modinfo_file:
        json.dump(info, modinfo_file)

install_mod("hypa_legion")
install_mod("hypa")
install_mod("hypa_thorosmen")
# install_mod("hypa_celestial_exp")
install_mod("hypa_telemazer")