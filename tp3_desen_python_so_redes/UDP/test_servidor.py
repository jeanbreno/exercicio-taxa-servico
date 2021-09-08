import socket
import psutil
import pickle
import os

HOST = 'localhost' # Endereco IP do Servidor
PORT = 5000                 # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print('Esperando receber na porta', PORT, '...')
(msg, cliente) = udp.recvfrom(1024)

total_disk = psutil.disk_usage('C:\\').total
free_disk = psutil.disk_usage('C:\\').free          

tupla_msg = (total_disk, free_disk)            
bytes_tupla = pickle.dumps(tupla_msg)
udp.sendto(bytes_tupla, orig)


udp.close()