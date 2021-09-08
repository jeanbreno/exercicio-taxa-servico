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

nome_arquivo = conexao.recv(1024).decode('ascii')

if os.path.exists(nome_arquivo):
    if os.path.isfile(nome_arquivo):
        tam_arq = os.stat(nome_arquivo).st_size
        bytes_tam = pickle.dumps(tam_arq)
        conexao.send(bytes_tam)

        requisicao = conexao.recv(1024).decode('utf-8')
        try:
            if requisicao == '1':
                with open(nome_arquivo, 'rb') as arquivo:
                    for data in arquivo.readlines():
                        conexao.send(data)
                        print('Enviando... ')
                        time.sleep(2)
                        
                    print('Enviado!')
            elif requisicao == '2':
                print("Fechando conexão. Arquivo não transmitido. \n")
        except:
            pass
    else:
        pass
else:
    print("Arquivo não existe. \n")

servidor.close()
