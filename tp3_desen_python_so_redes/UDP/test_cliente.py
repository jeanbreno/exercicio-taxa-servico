import socket
import psutil
import pickle
import os

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

HOST = 'localhost'  # Endereco IP do Servidor
PORT = 5000                  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
msg = 'oi'
udp.sendto (msg.encode('ascii'), dest)

resp = udp.recvfrom(1024)
print(resp.decode('ascii'))

tup = pickle.loads(resp)
lis = list(tup) 
total = format_memory(lis[0])
livre = format_memory(lis[1])
texto = f'Total: {total:.2f} GB\nLivre: {livre:.2f} GB'
print(texto)

udp.close()