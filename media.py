qtd = int(input("\nDigite quantas notas deseja calcular: "))
soma = 0
somapeso = 0
lista = []
for i in range(0,qtd,1):
    n1 = float(input(f"\nDigite a nota {i+1}: "))
    lista.append(n1)
    p = float(input(f"\nDigite o peso da nota {i+1}: "))
    soma = soma + n1 * p
    somapeso = somapeso + p


media = soma/somapeso
print(str(f"\nSuas notas são: {lista}").replace('[','| ').replace(']',' |'))
print(f"\nSua média ponderada é: {media:.1f}")

