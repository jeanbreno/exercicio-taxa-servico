def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

lista = [5, 8, 9, 10]
for i in lista:
    result = fatorial(i)
    print(result)