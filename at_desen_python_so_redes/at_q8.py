import time, random

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

N = int(input("Entre com o tamanho do vetor: "))

# Captura tempo inicial
t_inicio = float(time.time())

# Gera lista com valores aleatórios
lista = []
for i in range(N):
    lista.append(random.randint(0, 40))

# Faz o cálculo da soma dos valores do vetor/lista
#soma = 0
for i in lista:
    result = fatorial(i)
    print(f"Fatorial de {i}:  {result}")
# Captura tempo final

t_fim = float(time.time())

# Imprime o resultado e o tempo de execução

print("Lista:", lista)
print("Tempo total:", t_fim - t_inicio)