# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:00:56 2021

@author: 009671631
"""

import os 

files = {}
for i in os.listdir(os.chdir('.')):
    files[i] = []
    files[i].append(os.stat(i).st_size)
    kb = files[i][0]/1000
    texto = f'{kb:.2f} KB'
    print(i, texto)

     