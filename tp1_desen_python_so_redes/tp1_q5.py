# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 19:40:49 2021

@author: 009671631
"""

import os

quest = input("Digite: ")
if os.path.exists(quest):
  if os.path.isfile(quest):
      print(quest, 'existe e é um arquivo.')
  else:
      print(quest, 'existe, mas não é um arquivo.')
else:
  print(quest, 'não existe!')