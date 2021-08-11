# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:18:46 2021

@author: 009671631
"""

import psutil 

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

disco = psutil.disk_usage('.')
total = format_memory(disco.free)

print(f"Disco(armazenamento disponível): {total} GB")


