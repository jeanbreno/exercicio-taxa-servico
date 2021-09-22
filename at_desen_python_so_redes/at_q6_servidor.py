# -*- coding: utf-8 -*-

import socket
import os
import pickle
import time

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
porta = 8881
origem = host, porta

servidor.bind(origem)
servidor.listen(1)
print("Aguardando conexão... \n")

conexao, endereco = servidor.accept()
print(f"Conectado. \n")

nome_dir = conexao.recv(1024).decode('ascii')

l = []
if os.path.exists(nome_dir):
    for i in os.listdir(os.chdir(nome_dir)):
        if os.path.isfile(i):
            l.append(i)
        else:
            pass
    bytes_tam = pickle.dumps(l)
    conexao.send(bytes_tam)
else:
    erro = "Diretório não existe. \n"
    bytes_erro = pickle.dumps(erro)
    conexao.send(bytes_erro)
print("Fechando conexão...")
servidor.close()