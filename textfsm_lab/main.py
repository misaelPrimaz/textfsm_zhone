import os
import textfsm

local_path = os.path.dirname(__file__)
files_path = f'{local_path}/outputs'
templates_path = f'{local_path}/templates'
files = os.listdir(files_path)

for file in files:
    with open(f'{files_path}/{file}') as f:
        output = f.read()
    print(output)
    with open(f"{templates_path}/{file.replace('.txt', '.textfsm')}") as t:
        template = textfsm.TextFSM(t)
    fsm_result = template.ParseText(output)
    print(f'Result: {fsm_result}')
    input('Pressione algo para ir para o próximo arquivo...')