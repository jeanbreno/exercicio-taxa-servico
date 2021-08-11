# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:24:48 2021

@author: 009671631
"""

'''
import os

name_file = input("Nome do arquivo: ")
os.system("notepad")
'''

import subprocess

name_file = input("Nome do arquivo: ")
print(subprocess.run(["notepad", name_file]))