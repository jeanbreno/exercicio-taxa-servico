# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

#arquivos = open('arquivo.txt', 'w')

def rotacionar(texto,qtd):
    info = texto[qtd:], texto[:qtd]
    return info


texto = 'Ola, tudo bem'
qtd = 6
oi = rotacionar(texto, qtd)
print(oi)

for line in reversed(list(open("arquivo.txt"))):
    print(line.rstrip())

