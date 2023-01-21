import gen_core
import json
import os
import shutil

units = gen_core.units

tools = gen_core.tools

base_directory = gen_core.stage_path + "/"

gen = "redenbacher-ex/"

if os.path.isdir(gen):
    shutil.rmtree(gen)

shutil.copytree("export", gen, dirs_exist_ok=True)

for i in units:
    with open(base_directory + i) as k:
        unit = json.load(k)
        if "production" in unit:
            if "metal" in unit["production"]:
                unit["production"]["metal"] = unit["production"]["metal"] * 10
        if "storage" in unit:
            if "metal" in unit["storage"]:
                unit["storage"]["metal"] = unit["storage"]["metal"] * 10

        if "factory_cooldown_time" in unit:
            unit["factory_cooldown_time"] = unit["factory_cooldown_time"] / 10
        if "wait_to_rolloff_time" in unit:
            unit["wait_to_rolloff_time"] = unit["wait_to_rolloff_time"] / 10

        if "navigation" in unit:
            if "move_speed" in unit["navigation"]:
                unit["navigation"]["move_speed"] = int(unit["navigation"]["move_speed"] * 1.5)
            if "acceleration" in unit["navigation"]:
                unit["navigation"]["acceleration"] = int(unit["navigation"]["acceleration"] * 1.5)
            if "turn_speed" in unit["navigation"]:
                unit["navigation"]["turn_speed"] = int(unit["navigation"]["turn_speed"] * 1.5)

        new_filename = gen + i
        new_dirname = os.path.dirname(new_filename)
        if not os.path.isdir(new_dirname):
            os.makedirs(new_dirname)

        with open(new_filename, 'w+') as out:
            json.dump(unit, out)

for i in tools:
    with open(base_directory + i) as k:
        tool = json.load(k)

        if "construction_demand" in tool:
            if "metal" in tool["construction_demand"]:
                tool["construction_demand"]["metal"] = tool["construction_demand"]["metal"] * 10

        if "rate_of_fire" in tool:
            tool["rate_of_fire"] = tool["rate_of_fire"] * 1.5

        if "pitch_rate" in tool:
            tool["pitch_rate"] = tool["pitch_rate"] * 1.5

        if "yaw_rate" in tool:
            tool["yaw_rate"] = tool["yaw_rate"] * 1.5
        
        if "ammo_source" in tool:
            if tool["ammo_source"] == "metal":
                if "ammo_demand" in tool:
                    tool["ammo_demand"] = tool["ammo_demand"] * 1.5
            else:
                if "ammo_per_shot" in tool and "ammo_capacity" in tool:
                    tool["ammo_per_shot"] = tool["ammo_per_shot"] / 1.5
                    tool["ammo_capacity"] = tool["ammo_capacity"] / 1.5

        new_filename = gen + i
        new_dirname = os.path.dirname(new_filename)
        if not os.path.isdir(new_dirname):
            os.makedirs(new_dirname)

        with open(new_filename, 'w+') as out:
            json.dump(tool, out)

def write_altered_file(json_data, file_path):
    new_filename = os.path.join(gen, file_path)
    with open(new_filename, 'w+') as out:
        json.dump(json_data, out)

commander_path = "pa/units/commanders/base_commander/base_commander.json"
with open(os.path.join(gen, commander_path)) as unit_file:
    unit = json.load(unit_file)
    unit["max_health"] = unit["max_health"] * 15
    unit["build_metal_cost"] = unit["build_metal_cost"] * 15
    write_altered_file(unit, commander_path)

commander_weapons = [
    "base_commander_tool_weapon.json",
    "base_commander_tool_aa_weapon.json",
    "base_commander_tool_torpedo_weapon.json"
]
for weapon_name in commander_weapons:
    weapon_path = os.path.join("pa/units/commanders/base_commander/", weapon_name)
    with open(os.path.join(gen, weapon_path)) as tool_file:
        tool = json.load(tool_file)
        tool["rate_of_fire"] = tool["rate_of_fire"] * 10
        write_altered_file(tool, weapon_path)

uber_cannon_path = "pa/tools/uber_cannon/uber_cannon.json"
with open(os.path.join(gen, uber_cannon_path)) as tool_file:
    tool = json.load(tool_file)
    tool["rate_of_fire"] = tool["rate_of_fire"] * 3
    tool["ammo_per_shot"] = tool["ammo_per_shot"] // 5
    write_altered_file(tool, uber_cannon_path)

lob_tool_path = "pa/units/land/artillery_unit_launcher/artillery_unit_launcher_tool_weapon.json"
with open(os.path.join(gen, lob_tool_path)) as tool_file:
    tool = json.load(tool_file)
    tool["ammo_demand"] = tool["ammo_demand"] * 10
    tool["rate_of_fire"] = tool["rate_of_fire"] * 10
    write_altered_file(tool, lob_tool_path)

unit_cannon_path = "pa/units/land/unit_cannon/unit_cannon.json"
with open(os.path.join(gen, unit_cannon_path)) as unit_file:
    unit = json.load(unit_file)
    unit["factory"]["spawn_points"] = ["socket_build"] * (len(unit["factory"]["spawn_points"]) * 10)
    write_altered_file(unit, unit_cannon_path)

unit_cannon_weapon_path = "pa/units/land/unit_cannon/unit_cannon_tool_weapon.json"
with open(os.path.join(gen, unit_cannon_weapon_path)) as tool_file:
    tool = json.load(tool_file)
    tool["rate_of_fire"] = tool["rate_of_fire"] * 5
    write_altered_file(tool, unit_cannon_weapon_path)

star_cannon_path = "pa/units/orbital/l_orbital_dropper/l_orbital_dropper.json"
if star_cannon_path in units:
    with open(os.path.join(gen, star_cannon_path)) as unit_file:
        unit = json.load(unit_file)
        unit["factory"]["spawn_points"] = ["bone_rotate"] * (len(unit["factory"]["spawn_points"]) * 10)
        write_altered_file(unit, star_cannon_path)

    star_cannon_weapon_path = "pa/units/orbital/l_orbital_dropper/l_orbital_dropper_tool_weapon.json"
    with open(os.path.join(gen, star_cannon_weapon_path)) as tool_file:
        tool = json.load(tool_file)
        tool["rate_of_fire"] = tool["rate_of_fire"] * 5
        write_altered_file(tool, star_cannon_weapon_path)