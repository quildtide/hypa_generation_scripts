import json
import os.path
import urllib.request as req
import zipfile
import tempfile
import shutil

from pa_directory import pa_path

dl_path = "download"
stage_path = "stage"

def mount_hypa_stage(mod_urls, keep_base=False):
    for (mod, mod_url) in mod_urls.items():
        # download and unzip mods
        mod_folder = os.path.join(dl_path, mod)

        if os.path.isdir(mod_folder):
            # don't redownload if mod already downloaded
            # clear downloads if need to update version
            continue

        with req.urlopen(mod_url) as resp:
            with tempfile.TemporaryFile() as tmp_zip:
                shutil.copyfileobj(resp, tmp_zip)

                with zipfile.ZipFile(tmp_zip) as zf:
                    names = zf.namelist()
                    if "modinfo.json" in names:
                        zf.extractall(mod_folder)
                    else: # modinfo not in top level
                        firstpath = names[0].split("/")[0]
                        zf.extractall(dl_path)
                        os.rename(os.path.join(dl_path, firstpath), os.path.join(dl_path, mod))


    mod_priorities = {}
    mod_order = list()

    for mod in mod_urls.keys():
        mod_folder = os.path.join(dl_path, mod)
        
        # high priority mounts first; low priority overrides later!
        with open(os.path.join(mod_folder, "modinfo.json")) as infile:
            modinfo = json.load(infile)
            if "priority" in modinfo:
                priority = modinfo["priority"]
            else:
                priority = 100

            mod_priorities[mod] = priority

            if len(mod_order) == 0:
                mod_order.append(mod)
            elif priority < mod_priorities[mod_order[-1]]:
                # lowest mod priority seen so far
                mod_order.append(mod)
            else:
                for (i, m) in enumerate(mod_order):
                    if priority > mod_priorities[m]:
                        mod_order.insert(i, mod)
                        break
        
    # create aggregate unit list
    unit_list_path = os.path.join(pa_path, "pa_ex1/units/unit_list.json")

    with open(unit_list_path) as unit_list:
        unit_set = set(json.load(unit_list)['units'])

    for mod in mod_order:
        unit_list_path = os.path.join(dl_path, mod, "pa/units/unit_list.json")

        with open(unit_list_path) as unit_list:
            mod_units = set(json.load(unit_list)['units'])
            unit_set = unit_set.union(mod_units)

    units = [x[1:] for x in unit_set] # remove starting / from filepath

    # mount PA, Titans, and mod files in stage/
    if os.path.isdir(stage_path):
        shutil.rmtree(stage_path)

    os.mkdir(stage_path)

    tools = []

    def update_tool_list(unit_path):
        with open(unit_path) as unitfile:
            try:
                unit = json.load(unitfile)
            except:
                print(unitfile)

            if "tools" in unit:
                for j in unit['tools']:
                    tools.append(j['spec_id'])

    def copyfile_w_dir(src, dst):
        os.makedirs(os.path.dirname(dst), exist_ok = True)
        shutil.copyfile(src, dst)

    if keep_base:
    # mount PA and Titans unit/tool .jsons if we want to include them

        for unit in units:
            # There is a chance that a mod might bring in a unit defined in
            # the base game but which is absent in the base unit_list.
            # i.e. stinger or deepspace radar
            # Not a problem unless the unit isn't redefined in the mod.
            # However, this script protects against that just in case.
            vanilla_path = os.path.join(pa_path, unit)
            titans_path = os.path.join(pa_path, 'pa_ex1' + unit[2:])

            out_path = os.path.join(stage_path, unit)

            if os.path.isfile(titans_path):
                update_tool_list(titans_path)
                copyfile_w_dir(titans_path, out_path)
            elif os.path.isfile(vanilla_path):
                update_tool_list(vanilla_path)
                copyfile_w_dir(vanilla_path, out_path)

        tools = [x[1:] for x in tools]
        tools.append("pa/units/commanders/base_commander/base_commander_tool_weapon.json")

        for tool in tools:
            # There is a chance that a mod might use a tool defined in
            # the base game but which is not directly used by any unit
            # we've moved to stage/.
            # This is a problem but this script currently makes no attempt
            # to address this potential issue.
            vanilla_path = os.path.join(pa_path, tool)
            titans_path = os.path.join(pa_path, "pa_ex1" + tool[2:])

            out_path = os.path.join(stage_path, tool)

            if os.path.isfile(titans_path):
                copyfile_w_dir(titans_path, out_path)
            elif os.path.isfile(vanilla_path):
                copyfile_w_dir(vanilla_path, out_path)    

    # mount mod files in stage/
    for mod in mod_order:
        # There is a chance that modded units may be in weird places.
        # Mods are relatively small so we can mount them in their 
        # entirety just in case.
        shutil.copytree(os.path.join(dl_path, mod), stage_path, dirs_exist_ok=True)


    tools = [] # wipe contents to avoid duplicates

    # update tool list
    for unit in units:
        update_tool_list(os.path.join(stage_path, unit))

    tools = [x[1:] for x in tools]
    tools.append("pa/units/commanders/base_commander/base_commander_tool_weapon.json")

    if keep_base == False:
        # adjust unit and tool lists
        new_units = []
        for unit in units:
            if os.path.isfile(os.path.join(stage_path, unit)):
                new_units.append(unit)
        units = new_units
        
        new_tools = []
        for tool in tools:
            if os.path.isfile(os.path.join(stage_path, tool)):
                new_tools.append(tool)
        tools = new_tools

    return (units, tools)

def hypa_transform_units(units, stage_dir, out_dir):
    for i in units:
        with open(stage_dir + i) as k:
            unit = json.load(k)
            if "production" in unit:
                if "metal" in unit["production"]:
                    unit["production"]["metal"] = unit["production"]["metal"] * 2
            if "storage" in unit:
                if "metal" in unit["storage"]:
                    unit["storage"]["metal"] = unit["storage"]["metal"] * 2

            if "factory_cooldown_time" in unit:
                unit["factory_cooldown_time"] = unit["factory_cooldown_time"] / 2
            if "wait_to_rolloff_time" in unit:
                unit["wait_to_rolloff_time"] = unit["wait_to_rolloff_time"] / 2

            if "navigation" in unit:
                if "move_speed" in unit["navigation"]:
                    unit["navigation"]["move_speed"] = int(unit["navigation"]["move_speed"] * 1.5)
                if "acceleration" in unit["navigation"]:
                    unit["navigation"]["acceleration"] = int(unit["navigation"]["acceleration"] * 1.5)
                if "turn_speed" in unit["navigation"]:
                    unit["navigation"]["turn_speed"] = int(unit["navigation"]["turn_speed"] * 1.5)

            new_filename = out_dir + i
            new_dirname = os.path.dirname(new_filename)
            if not os.path.isdir(new_dirname):
                os.makedirs(new_dirname)

            with open(new_filename, 'w+') as out:
                json.dump(unit, out)

def hypa_transform_tools(tools, stage_dir, out_dir):
    for i in tools:
        with open(stage_dir + i) as k:
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
            
            if "ammo_source" in tool:
                if tool["ammo_source"] == "metal":
                    if "ammo_demand" in tool:
                        tool["ammo_demand"] = tool["ammo_demand"] * 1.5
                else:
                    if "ammo_per_shot" in tool and "ammo_capacity" in tool:
                        tool["ammo_per_shot"] = tool["ammo_per_shot"] / 1.5
                        tool["ammo_capacity"] = tool["ammo_capacity"] / 1.5

            new_filename = out_dir + i
            new_dirname = os.path.dirname(new_filename)
            if not os.path.isdir(new_dirname):
                os.makedirs(new_dirname)

            with open(new_filename, 'w+') as out:
                json.dump(tool, out)


def write_altered_file(json_data, file_path, out_dir):
    new_filename = os.path.join(out_dir, file_path)
    with open(new_filename, 'w+') as out:
        json.dump(json_data, out)