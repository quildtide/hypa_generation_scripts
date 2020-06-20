import json

import pa_directory

with open('unit_list.json') as unit_list:
    units = json.load(unit_list)['units']

for i in range(len(units)):
    try:
        titans = '/pa_ex1' + units[i][3:]
        with open(base_directory + titans) as t:
            units[i] = titans
    except:
        c = 0


tools = []

for i in units:
    filename = base_directory + i
    with open(filename) as unitfile:
        unit = json.load(unitfile)
        try:
            for j in unit['tools']:
                tools.append(j['spec_id'])
        except:
            c = 0

for i in range(len(tools)):
    try:
        titans = '/pa_ex1' + tools[i][3:]
        with open(base_directory + titans) as t:
            tools[i] = titans
    except:
        c = 0