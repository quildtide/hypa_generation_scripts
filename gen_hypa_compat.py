import gen_core
import os
import shutil

base_directory = gen_core.stage_path + "/"

def generic_mod_actions(mod_urls, export_dir, out_dir):
    # Prepare output directory
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)

    shutil.copytree(export_dir, out_dir, dirs_exist_ok=True)

    # mount stage and get unit and tool lists
    units, tools = gen_core.mount_hypa_stage(mod_urls, keep_base = False)

    # General Modifications
    gen_core.hypa_transform_units(units, base_directory, out_dir)
    gen_core.hypa_transform_tools(tools, base_directory, out_dir)


# Thorosmen
mod_urls = {
    "thorosmen": "https://github.com/ATLASLORD/Thorosmen/archive/refs/heads/main.zip",
}
generic_mod_actions(mod_urls, "export_thorosmen", "hypa_thorosmen/")


# Celestial Expansion
# mod_urls = {
#     "celestial_exp": "https://github.com/Planetary-Annihilation-Fandom/com.pa.expansion.celestial/archive/refs/heads/main.zip",
#     "celestial_exp_addon": "https://github.com/Planetary-Annihilation-Fandom/com.pa.expansion.celestial.additional/archive/refs/heads/main.zip"
# }
# generic_mod_actions(mod_urls, "export_celestial_exp", "hypa_celestial_exp/")

# Telemazer go BRRR
mod_urls = {
    "telemazer": "https://github.com/DAEDALUS-Modding/telemazer-go-brrr/releases/latest/download/telemazer-server.zip"
}
generic_mod_actions(mod_urls, "export_telemazer", "hypa_telemazer/")

# Legion
mod_urls = {
    "legion": "https://github.com/Legion-Expansion/com.pa.legion-expansion-server/archive/main.zip"
}
generic_mod_actions(mod_urls, "export_legion", "hypa_legion/")


# Write ZIP files
shutil.make_archive("hypa_thorosmen", "zip", "hypa_thorosmen")
shutil.make_archive("hypa_celestial_exp", "zip", "hypa_celestial_exp")
shutil.make_archive("hypa_telemazer", "zip", "hypa_telemazer")
shutil.make_archive("hypa_legion", "zip", "hypa_legion")