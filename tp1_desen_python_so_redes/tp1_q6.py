# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:55:08 2021

@author: 009671631
"""

import os

quest = input("Digite: ")
arq, ext = os.path.splitext(quest)

print(f"Nome do arquivo: {arq} \nExtensão do arquivo: {ext}")