#entrada de dados
consumo = float(input("Informe o valor total do consumo: R$ "))
while consumo < 0: #validações
    print("Valor inválido!")
    consumo = float(input("Informe novamente o valor total do consumo: R$ "))
if consumo == 0:
    print("Obrigado e até a próxima!")
    exit()

pessoas = int(input("Informe o total de pessoas: "))
while pessoas < 0: #validações
    print("Valor inválido!")
    pessoas = float(input("Informe novamente a quantidade total de pessoas: "))

percentual = int(input("Informe o percentual do serviço(0 a 100): "))
while percentual < 0 or percentual > 100: #validações
    print("Valor inválido!")
    percentual = float(input("Informe novamente o percentual do serviço: "))

percentualResult = (consumo * percentual) / 100

#definindo funções
def valor_total(consumo, percentualResult):
    totalConta = consumo + percentualResult
    return totalConta
    
def conta_dividida(totalConta, pessoas):
    contaDividida = totalConta / pessoas
    return contaDividida

total = (valor_total(consumo, percentualResult))
dividida = conta_dividida(valor_total(consumo, percentualResult), pessoas)

valorTotal = total
#valorTotal = str(total) 
#valorTotal.replace('.', ',')
#valorTotal = float(total)
#print(valorTotal)
#valorDividida = dividida
#valorPercentual = percentualResult


#saída de dados
print("De acordo com o valor informado, a taxa de serviço será de R$ {:.2f}." .format(percentualResult))
print("O valor total da conta com {} % da taxa de serviço será de R$ {:.2f}." .format(percentual, valorTotal))
print("A conta de R$ {:.2f}, dividido por {} pessoas, será de R$ {:.2f} para cada." .format(valorTotal, pessoas, dividida))

