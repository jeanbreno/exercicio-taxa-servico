# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:04:36 2021

@author: 009671631
"""

import psutil, time

psutil.cpu_percent(percpu=True)

for i in range(20):
  time.sleep(0.1)
  print(psutil.cpu_percent(percpu=True))