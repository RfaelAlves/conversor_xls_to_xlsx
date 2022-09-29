import os
import json
import pandas as pd

# importando configurações:

root_dir =  os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([root_dir, 'config.json'])

with open(config_path, encoding='utf8') as config_file:
    config = json.load(config_file)
    config = config['config']


#Variaveis:

caminho_ori = config['arquivos_ori']
caminho_conv = config['arquivos_conv']
list_arquivos = os.listdir(caminho_ori)

def converter_arquivos():
    for arquivo in list_arquivos:
        df = pd.read_excel(caminho_ori+'\\'+str(arquivo), engine='xlrd')
        df.to_excel(caminho_conv+'\\'+str(arquivo)+".xlsx",index=False)

converter_arquivos()

print('finalizado!')
