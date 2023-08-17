a = int(input("Digite sua idade: "))

if a>=70:
    print("Seu voto é opcional")

elif a>=18 and a<=69:
    print("Voto obrigatório")

elif a>=16 and a<=17:
    print("Seu voto é opcional")

else:
    print("Você não pode votar")
