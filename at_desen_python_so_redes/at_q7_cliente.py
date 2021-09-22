# -*- coding: utf-8 -*-


import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000 

while True:
    msg_envio = input("Digite >  ")
    cliente.sendto(msg_envio.encode(), (HOST, PORT))

    msg_b, end_server = cliente.recvfrom(2048)
    print(msg_b.decode())


































'''

import socket

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = input("Entre com a mensagem: \n")

udp.sendto (msg.encode('ascii'), dest)


resp = udp.recvfrom(1024)
print(resp.decode('ascii'))

udp.close()

'''













'''
import socket
import pickle

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

# Cria o socket

host = 'localhost'
porta = 9991
destino = (host, porta)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(destino)

msg = str(input('Entre com a opção: \n > '))

while msg == 'm':
# Envia mensagem codificada em bytes ao servidor
    s.sendto(msg.encode('ascii'), destino)   

    resposta, endereco = s.recvfrom(1024)

    print("Recebida > ", str(resposta))

s.close()

'''












'''
    resp = s.recvfrom(1024)
    print(resp.decode('ascii'))
    
    tup = pickle.loads(resp)
    lis = list(tup) 
    total = format_memory(lis[0])
    livre = format_memory(lis[1])
    texto = f'Total: {total:.2f} GB\nLivre: {livre:.2f} GB'
    print(texto)

    print(str(erro))
    s.close()

    '''