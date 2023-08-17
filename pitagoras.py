a = int(input("Valor do cateto A: "))
b = int(input("Valor do cateto B: "))
h2 = (a**2)+(b**2)
h = (h2**0.5)
p = a+b+h
area = (a*b)/2

print(f"A Hipotenusa é: {h} ")
print(f"O Perímetro do triângulo é: {p:.1f} ")
print(f"A área do triângulo é: {area} ")