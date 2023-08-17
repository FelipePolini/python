while True:
    num1 = input("\nDigite um número inteiro: ")
    try:
        num1 = int(num1)
        break
    except:
        print("Valor inválido")
        continue

divisores = [2,3,5,7]

if num1 <= 0 or num1 == 1:
    print(f"\n{num1} não é primo")

elif num1 in divisores:
    print(f"\n{num1} é primo")

elif num1 % 2 != 0 and num1 % 3 !=0 and num1 % 5 !=0 and num1 % 7 !=0:
    print(f"\n{num1} é primo")

else:
    print(f"\n{num1} não é primo")

