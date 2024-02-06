import gen_core
import json
import os
import shutil

base_directory = gen_core.stage_path + "/"

# Prepare output directory
gen = "hypa/"

if os.path.isdir(gen):
    shutil.rmtree(gen)

shutil.copytree("export", gen, dirs_exist_ok=True)


# mount stage and get unit and tool lists
mod_urls = {
    # "legion": "https://github.com/Legion-Expansion/com.pa.legion-expansion-server/archive/main.zip",
    "2w": "https://github.com/Anonemous2/pa.mla.unit.addon/archive/master.zip",
    "s17": "https://github.com/DAEDALUS-Modding/Section-17/releases/latest/download/s17-server.zip",
    "dozer": "https://github.com/DAEDALUS-Modding/Dozer/archive/release.zip",
    "bugs": "https://github.com/Ferret-Master/Bug-Faction/archive/refs/heads/main.zip",
    # "scenario_units": "https://github.com/Ferret-Master/Scenario-Server/archive/refs/heads/release.zip",
    "upgradable_turrets": "https://github.com/BotWhan/com.pa.upgradable-turrets/archive/main.zip"
}
units, tools = gen_core.mount_hypa_stage(mod_urls, keep_base = True)


# General Modifications
gen_core.hypa_transform_units(units, base_directory, gen)
gen_core.hypa_transform_tools(tools, base_directory, gen)

# Special Modifications

# Commander
commander_paths = [
    "pa/units/commanders/base_commander/base_commander.json",
    "pa/units/commanders/base_bug_commander/base_commander.json"
]
for commander_path in commander_paths:
    with open(os.path.join(gen, commander_path)) as unit_file:
        unit = json.load(unit_file)
        unit["max_health"] = unit["max_health"] * 2
        unit["build_metal_cost"] = unit["build_metal_cost"] * 2
        gen_core.write_altered_file(unit, commander_path, gen)

# Lob
lob_tool_path = "pa/units/land/artillery_unit_launcher/artillery_unit_launcher_tool_weapon.json"
with open(os.path.join(gen, lob_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_demand"] = tool["ammo_demand"] * 2
    tool["rate_of_fire"] = tool["rate_of_fire"] * 2
    gen_core.write_altered_file(tool, lob_tool_path, gen)

# Bug Matriarch
special_tool_path = "pa/units/land/bug_matriarch/bug_matriarch_weapon.json"
with open(os.path.join(gen, special_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_demand"] = tool["ammo_demand"] * 2
    gen_core.write_altered_file(tool, special_tool_path, gen)

# S17 Dox Materializer
special_tool_path = "pa/units/paeiou/dox_materializer/weapon.json"
with open(os.path.join(gen, special_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_per_shot"] = tool["ammo_per_shot"] / 2
    tool["ammo_capacity"] = tool["ammo_capacity"] / 2
    gen_core.write_altered_file(tool, special_tool_path, gen)

# S17 Sigma, Slammer Dropper
special_tool_path = "pa/units/paeiou/sigma/dropper_weapon.json"
with open(os.path.join(gen, special_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_demand"] = tool["ammo_demand"] * 2
    tool["rate_of_fire"] = tool["rate_of_fire"] * 2
    gen_core.write_altered_file(tool, special_tool_path, gen)

# S17 Sigma, Avenger Hangar
special_tool_path = "pa/units/paeiou/sigma/avenger_weapon.json"
with open(os.path.join(gen, special_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_demand"] = tool["ammo_demand"] * 2
    tool["rate_of_fire"] = tool["rate_of_fire"] * 2
    gen_core.write_altered_file(tool, special_tool_path, gen)
    
# Temporary Bug Matriarch Death Spawner Fix
special_tool_path = "pa/units/land/bug_matriarch/bug_matriarch_death_spawner.json"
with open(os.path.join(gen, special_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_id"][0]["id"] = "/pa/units/land/bug_matriarch/bug_matriarch_ammo.json"
    gen_core.write_altered_file(tool, special_tool_path, gen)


# Write ZIP file
shutil.make_archive("hypa", "zip", gen)
