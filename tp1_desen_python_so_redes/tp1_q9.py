# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:14:31 2021

@author: 009671631
"""

import os, time

files = {}
lista = os.listdir()

for i in lista:
    files[i] = []
    files[i].append(time.ctime(os.stat(i).st_mtime))

for w, q in files.items():
    print(w + " // Modificado em: "+str(q))
