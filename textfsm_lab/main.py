import os
import textfsm

local_path = os.path.dirname(__file__)
files_path = f'{local_path}/outputs'
templates_path = f'{local_path}/templates'
files = os.listdir(files_path)


file = "onu_showall_slot.txt"

with open(f'{files_path}/{file}') as f:
    output = f.read()
print(output)
with open(f"{templates_path}/{file.replace('.txt', '.textfsm')}") as t:
    template = textfsm.TextFSM(t)
fsm_result = template.ParseText(output)
print(f'Headers: {template.header}')

showall = []
for row in fsm_result:
    d = {}
    row[3] = row[3].replace(' ', '')
    row[4] = row[4].replace('ZNTS ', '')
    row[4] = row[4].replace(' ', '')
    for i, value in enumerate(row):
        d.update({template.header[i]: row[i]})
    showall.append(d)

print([(registro['name'], registro['serial']) for registro in showall if registro.get('serial')])

#   ^\s+${id}\s+${name}\s+${enabled}\s${model}\s+${serial}\s+${omci} -> Record
