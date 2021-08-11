# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:52:07 2021

@author: 009671631
"""

import os


quest = input("Digite o nome do diretório: ")
if os.path.exists(quest):
    caminho_abs = os.path.abspath(quest)
    caminho_dir = os.path.dirname(caminho_abs)
    print(f"O caminho absoluto é: \n{caminho_dir}")
else:
    print("Não existe.")

#print(os.getcwd())
#print(access_complet)
#print(os.path.abspath(item_source))
#print(os.path.dirname(item_source))