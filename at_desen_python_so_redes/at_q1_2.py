# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

import psutil
import os # para o system('cls')
import time # para o sleep

def func_comparacao(l):
    return(l['cpu_percent'])

def format_memory(info):
    return round(info/(1024*1024*1024), 2)
    
for i in range(11):
    lista = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
            lista.append(pinfo)
        except psutil.NoSuchProcess:
            pass

    os.system('cls')
    if lista:
        titulo = '{:<6}'.format("PID")
        titulo = titulo + '{:<20.19}'.format("Nome")
        titulo = titulo + '{:>6}'.format("%CPU")
        print(titulo)
        lista_ordenada = sorted(lista, key=func_comparacao,
        reverse=True)
        for i in lista_ordenada[0:15]:
            texto = '{:<6}'.format(i['pid'])
            texto = texto + '{:<20.19}'.format(i['name'])
            texto = texto + '{:>6}'.format(i['cpu_percent'])
            print(texto)
    time.sleep(1)

mem = psutil.virtual_memory()
total = format_memory(mem.total)
usado = format_memory(mem.used)
percent_m = mem.percent
nucleos = psutil.cpu_count()
l_cpu_percent = psutil.cpu_percent(interval=1, percpu=True)

print("\n---------------INFO-----------------")
print(f"\n\nQtd de núcleos: {nucleos}")
print(f"Percentual de uso da CPU por núcleo: {l_cpu_percent}")
print(f"Total de memória: {total} GB \nTotal Usado: {usado} GB \nPercentual usado: {percent_m} %")
input("\nDigite qualquer tecla para sair...\n")