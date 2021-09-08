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

nome_arquivo = str(input("Arquivo>"))
try:
    cliente.send(nome_arquivo.encode('ascii'))

    #resposta do servidor 
    resp = cliente.recv(1024)
    resp = pickle.loads(resp)
    kb = resp/1000
    print(f'Tamanho do {nome_arquivo}: {kb:.2f} KB')

    #imprimiu resposta e pergunta se quer transmitir
    print("Fazer a transmissão do arquivo? ")
    resp = str(input("\n1 - SIM \n2 - NAO \n> "))
    try:
        cliente.send(resp.encode('utf-8'))
        if resp == '1':
            with open(nome_arquivo, 'wb') as arquivo:
                while True:
                    data = cliente.recv(10000000)
                    print('Recebendo... ')
                    time.sleep(2)
                    
                    if not data:
                        print("Arquivo recebido.")
                        break
                        
        elif resp == '2':
            print("Fechando conexão. Arquivo não transmitido. \n")
    except:
        print("Erro inesperado. Fechando.")

except:
    print("Arquivo não existe. \n")

cliente.close()
