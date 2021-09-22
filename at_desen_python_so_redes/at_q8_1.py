from multiprocessing import Pool


def factorial(arr):
    result = 1
    for i in arr:
        result *= i
    return result


"""Breaking input number into chunks and calculating factorial of each chunk"""
def main(n, workers):
    # Creating a process pool with number of processes given when main function is called
    p = Pool(processes=workers)
    # Splitting the given number into array consisting of arrays with numbers
    numbers = range(1, n+1)
    slices = [numbers[i::workers] for i in range(workers)]
    # Mapping the slices array to processes where factorial of each chunk is calculated
    chunks = p.map(factorial, slices)
    p.close()
    p.join()

    # Getting the result
    result = 1
    for c in chunks:
        result *= c

    return result

print(main(2,1))















'''import threading
import math

class f(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        global result
        temp = math.factorial(self.num)
        print("%s: calculate %d's factorial is %d" %(self.name,self.num,temp))
        result += temp

result = 0
threads = []

def test():
    for i in range(1,6):
        t = f(i)
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()

if __name__ == '__main__':
    test()

    print ('The result is %d' %result )



'''






'''
import threading, time, random

def somaThread(lista, soma_parcial, id):
    soma = 0
    for i in lista:
        soma = soma + i
    soma_parcial[id] = soma

N = int(input("Entre com o tamanho do vetor: "))

# Captura tempo inicial
t_inicio = float(time.time())

# Gera lista com valores aleatórios
lista = []
for i in range(N):
    lista.append(random.randint(2, 30))

Nthreads = 4 # Número de threads a ser criado


# Vetor para salvar a soma parcial de cada thread
soma_parcial = Nthreads * [0]
lista_threads = []

for i in range(Nthreads):
    ini = i * int(N/Nthreads) # início do intervalo da lista

    fim = (i + 1) * int(N/Nthreads) # fim do intervalo da lista

    t = threading.Thread(target=somaThread, args=(lista[ini:fim],soma_parcial, i))

    t.start() # inicia thread

    lista_threads.append(t) # guarda a thread


for t in lista_threads:
    t.join() # Espera as threads terminarem


soma = 0
for i in soma_parcial:
    soma = soma + i

# Captura tempo final
t_fim = float(time.time())

# Imprime o resultado e o tempo de execução
print(lista)
print("Soma:", soma)
print("Tempo total:", t_fim - t_inicio)
'''

