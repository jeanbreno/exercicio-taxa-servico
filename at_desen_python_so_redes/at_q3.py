
# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""
import os

arquivos = open('arquivos.txt', 'w')
dir_corrente = os.getcwd()

info = f"Caminho dos arquivos: {dir_corrente}\n\n"
arquivos.write(info)

files = {}
f = {}
for i in os.listdir(os.chdir('.')):
    files[i] = []
    files[i].append(os.stat(i).st_size)
    kb = files[i][0]/1000
    texto = f"{kb:.2f} KB"
    f[i]=texto

for k in sorted(f, reverse=True):
    info = f"> {k} | {f[k]}\n"
    arquivos.write(info)

arquivos.close