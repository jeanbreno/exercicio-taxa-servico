import socket
import pickle

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host = 'localhost'
porta = 9991
destino = (host, porta)

msg = str(input('Entre com a opção: \n1 - DISCO \n> '))
# Envia mensagem codificada em bytes ao servidor
s.sendto(msg.encode('ascii'), destino)   

try:
    if msg == '1':
        resp = s.recvfrom(1024)
        #print(resp.decode('ascii'))
        
        tup = pickle.loads(resp)
        lis = list(tup) 
        total = format_memory(lis[0])
        livre = format_memory(lis[1])
        texto = f'Total: {total:.2f} GB\nLivre: {livre:.2f} GB'
        print(texto)

    else:
        print("n pegou o 1")

    s.close()

except Exception as erro:
    print(str(erro))