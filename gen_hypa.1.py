import gen_core
import json
import os

units = gen_core.units

tools = gen_core.tools

base_directory = gen_core.base_directory

for i in units:
    with open(base_directory + i) as k:
        unit = json.load(k)
        if "production" in unit:
            if "metal" in unit["production"]:
                unit["production"]["metal"] = unit["production"]["metal"] * 2
        if "storage" in unit:
            if "metal" in unit["storage"]:
                unit["storage"]["metal"] = unit["storage"]["metal"] * 2

        if "factory_cooldown_time" in unit:
            unit["factory_cooldown_time"] = unit["factory_cooldown_time"] / 2

        if "navigation" in unit:
            if "move_speed" in unit["navigation"]:
                unit["navigation"]["move_speed"] = int(unit["navigation"]["move_speed"] * 1.5)
            if "acceleration" in unit["navigation"]:
                unit["navigation"]["acceleration"] = int(unit["navigation"]["acceleration"] * 1.5)
            if "turn_speed" in unit["navigation"]:
                unit["navigation"]["turn_speed"] = int(unit["navigation"]["turn_speed"] * 1.5)


        if i[0:7] == '/pa_ex1':
            i = '/pa' + i[7:] 

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

        if "construction_demand" in tool:
            if "metal" in tool["construction_demand"]:
                tool["construction_demand"]["metal"] = tool["construction_demand"]["metal"] * 2

        if "rate_of_fire" in tool:
            tool["rate_of_fire"] = tool["rate_of_fire"] * 1.5
        if "pitch_rate" in tool:
            tool["pitch_rate"] = tool["pitch_rate"] * 1.5
        if "yaw_rate" in tool:
            tool["yaw_rate"] = tool["yaw_rate"] * 1.5

        if "ammo_demand" in tool:
            tool["ammo_demand"] = tool["ammo_demand"] * 1.5     


        if i[0:7] == '/pa_ex1':
            i = '/pa' + i[7:] 

        try:
            with open('hypa' + i, 'w+') as out:
                c = 0
        except:
            os.makedirs("/".join(('hypa' + i).split("/")[:-1]))

        with open('hypa' + i, 'w+') as out:
            json.dump(tool, out)