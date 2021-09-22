# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

import psutil as ps

def format_memory(info):
    return round(info/(1024*1024*1024), 2)


print('Lista de processos em execução: \n')

for proc in ps.process_iter():
    info = proc.as_dict(attrs=['pid', 'name'])
    print('Processo: {} (PID: {})'.format(info['pid'], info['name']))

nucleos = ps.cpu_count()
l_cpu_percent = ps.cpu_percent(interval=1, percpu=True)

mem = ps.virtual_memory()
total = format_memory(mem.total)
usado = format_memory(mem.used)
percent_m = mem.percent
print("\n---------------INFO-----------------")
print(f"\n\nQtd de núcleos: {nucleos}")
print(f"Percentual de uso da CPU por núcleo: {l_cpu_percent}")
print(f"Total de memória: {total} GB \nTotal Usado: {usado} GB \nPercentual usado: {percent_m} %")
input("\nDigite qualquer tecla para sair...\n")