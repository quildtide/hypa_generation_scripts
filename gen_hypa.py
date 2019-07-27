import gen_core
import json
import os

units = gen_core.units

tools = gen_core.tools

base_directory = gen_core.base_directory

for i in units:
    with open(base_directory + i) as k:
        unit = json.load(k)
        if "build_metal_cost" in unit:
            unit["build_metal_cost"] = unit["build_metal_cost"] // 2
        if "factory_cooldown_time" in unit:
            unit["factory_cooldown_time"] = unit["factory_cooldown_time"] // 2

        if "navigation" in unit:
            if "move_speed" in unit["navigation"]:
                unit["navigation"]["move_speed"] = int(unit["navigation"]["move_speed"] * 1.5)
            if "acceleration" in unit["navigation"]:
                unit["navigation"]["acceleration"] = int(unit["navigation"]["acceleration"] * 1.5)
            if "turn_speed" in unit["navigation"]:
                unit["navigation"]["turn_speed"] = int(unit["navigation"]["turn_speed"] * 1.5)

        try:
            with open('hypa' + i, 'w+') as out:
                c = 0
        except:
            os.makedirs("/".join(('hypa' + i).split("/")[:-1]))

        with open('hypa' + i, 'w+') as out:
            json.dump(unit, out)

for i in tools:
    with open(base_directory + i) as k:
        tool = json.load(k)
        if "rate_of_fire" in tool:
            tool["rate_of_fire"] = tool["rate_of_fire"] * 1.5
        if "pitch_rate" in tool:
            tool["pitch_rate"] = tool["pitch_rate"] * 1.5
        if "yaw_rate" in tool:
            tool["yaw_rate"] = tool["yaw_rate"] * 1.5
        if "ammo_per_shot" in tool:
            tool["ammo_per_shot"] = tool["ammo_per_shot"] // 1.5
        if "ammo_capacity" in tool:
            tool["ammo_capacity"] = tool["ammo_capacity"] // 1.5

        try:
            with open('hypa' + i, 'w+') as out:
                c = 0
        except:
            os.makedirs("/".join(('hypa' + i).split("/")[:-1]))

        with open('hypa' + i, 'w+') as out:
            json.dump(tool, out)