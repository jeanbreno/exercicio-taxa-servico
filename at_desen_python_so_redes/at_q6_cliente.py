# -*- coding: utf-8 -*-

import socket
import pickle
import os
import time

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
porta = 8881
destino = host, porta

cliente.connect(destino)
print("Conectado. \n")

nome_dir = str(input("Diretório > "))
try:
    cliente.send(nome_dir.encode('ascii'))

    #resposta do servidor 
    resp = cliente.recv(1024)
    resp = pickle.loads(resp)
    print(resp)
######################

except:
    print("Arquivo não existe. \n")

cliente.close()