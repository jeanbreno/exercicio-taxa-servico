
import socket
import psutil
import pickle
import os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
porta = 9991
origem = (host, porta)

socket_servidor.bind(origem)
print("Servidor ", host, "esperando conexão na porta", porta)

msg, endereco = socket_servidor.recvfrom(1024)

t = msg, endereco
l = list(t)
m = str(l[0].decode('ascii'))
print(m)


if m == '1':
    total_disk = psutil.disk_usage('C:\\').total
    free_disk = psutil.disk_usage('C:\\').free          
    
    tupla_msg = (total_disk, free_disk)            
    bytes_tupla = pickle.dumps(tupla_msg)
    socket_servidor.sendto(bytes_tupla, origem)
else:
    print("Erro.")


socket_servidor.close()
        