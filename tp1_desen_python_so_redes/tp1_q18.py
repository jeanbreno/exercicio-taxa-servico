# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:05:44 2021

@author: 009671631
"""

import psutil

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

mem = psutil.virtual_memory()
total = format_memory(mem.total)

print(f"Memória principal: {total} GB")

mem_swap = psutil.swap_memory()
total = format_memory(mem_swap.total)

print(f"Memória swap: {total} GB")