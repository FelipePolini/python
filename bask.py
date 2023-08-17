
a = int(input("\nDigite um número: "))
b = int(input("\nDigite um número: "))
c = int(input("\nDigite um número: "))

delta = b**2 - 4*a*c
x1 = (-b + (delta**0.5))/2*a
x2 = (-b - (delta**0.5))/2*a

if delta > 0:
    print(f"\nPossui duas raízes reais = {x1:.2f} e {x2:.2f}\n")
elif delta == 0:
    print(f"\nPossui uma raíz real = {x1:.2f}\n")
elif delta < 0:
    print(f"\nNão possui nenhuma raíz\n")