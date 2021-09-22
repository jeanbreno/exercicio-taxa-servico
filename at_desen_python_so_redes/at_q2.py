# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

import subprocess as sb
import time
import os

name_file = input("Nome do arquivo de texto: ")

if os.path.isfile(name_file):
    print(f"> abrindo arquivo {name_file}...")
    for i in range(3):
        time.sleep(1)
        print(">")
    sb.run(["notepad", name_file])
else:
    print("Arquivo não existe.")

