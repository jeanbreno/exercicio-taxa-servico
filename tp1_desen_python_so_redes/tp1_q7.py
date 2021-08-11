# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 07:32:11 2021

@author: 009671631
"""

import os

quest = input("Digite: ")
if os.path.exists(quest):
    caminho_abs = os.path.abspath(quest)
    caminho_dir = os.path.dirname(caminho_abs)
    print(f"O caminho absoluto é: \n{caminho_dir}")
else:
    print("Não existe.")
