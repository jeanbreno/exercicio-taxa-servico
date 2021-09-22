# -*- coding: utf-8 -*-

import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000
servidor.bind((HOST, PORT))

while True:
    msg_b, end_server = servidor.recvfrom(2048)
    msg_r = msg_b.decode().upper()
    
    servidor.sendto(msg_r.encode(), (HOST, PORT))

    print(msg_r)






'''
import socket

HOST = socket.gethostname() # Endereco IP do Servidor
PORT = 5000                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')

(msg, cliente) = udp.recvfrom(1024)
m = msg.decode('ascii')

print(cliente, m)

y = "memoria disponivel ..."

udp.sendto(y.encode('ascii'), orig)

udp.close()
input('Pressione qualquer tecla para sair...')


'''










'''
import socket
import psutil
import pickle
import os

host = 'localhost'
porta = 9991
origem = (host, porta)

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_servidor.bind(origem)
print("Servidor ", host, "esperando conexão na porta", porta)

while True:
    msg, endereco = socket_servidor.recvfrom(1024)
    print("Cliente: ", str(endereco))
    print("Msg: ", str(msg))
    
    #resposta
    
    resposta = "oiiii" + str(msg)
    socket_servidor.sendto(msg, endereco)
socket_servidor.close()
    #t = msg, endereco
    #l = list(t)
    #m = str(l[0].decode('ascii'))
    #print(m)
    
  '''  
    
'''
try:
    total_disk = psutil.disk_usage('C:\\').total
    free_disk = psutil.disk_usage('C:\\').free          
    
    tupla_msg = (total_disk, free_disk)            
    bytes_tupla = pickle.dumps(tupla_msg)
    socket_servidor.sendto(bytes_tupla, origem)
except:
    print("Fechando servidor...")
    socket_servidor.close()
'''