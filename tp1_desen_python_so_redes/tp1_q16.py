# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:52:45 2021

@author: 009671631
"""

import psutil

t = psutil.cpu_times(percpu=True)
print(t)