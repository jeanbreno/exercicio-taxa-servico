# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

def rotacionar(texto):
    return texto[::-1]

arquivos = open('arquivo.txt', 'r')

texto = arquivos.read()

info = rotacionar(texto)

arquivos.close()

print(info)
