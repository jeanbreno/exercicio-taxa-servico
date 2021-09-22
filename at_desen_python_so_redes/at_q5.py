# -*- coding: utf-8 -*-
"""
Criado em 21/09/2021

@author: Jean 
"""

a = open('a.txt', 'r')
b = open('b.txt', 'r')
c = open('c.txt', 'w')

for linha in a:
    n1 = linha.split()

for linha in b:
    n2 = linha.split()

l = []
for iA, iB in zip(n1, n2):
    l.append(int(iA) + int(iB))

c.write(str(l))

a.close
b.close
c.close
