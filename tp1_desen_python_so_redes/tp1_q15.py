# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:19:04 2021

@author: 009671631
"""

import psutil, time


num_pid = int(input("Número do PID: "))

pid_process = psutil.Process(num_pid)

name_process = pid_process.name()
user_name = pid_process.username()
time_create = time.ctime(pid_process.create_time())
mem_process = pid_process.memory_info()
kb = mem_process[0]/1000
texto = f"{kb:.2f} KB"


print(f"\nNome do processo: {name_process}"
      f"\nUsuário dono do processo: {user_name}"
      f"\nTempo de criação: {time_create}"
      f"\nUso de memória: {texto}"
      )