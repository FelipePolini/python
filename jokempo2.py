import random

print("Jokenpô")

jogadas = ("pedra", "papel", "tesoura")

player = input("Jogue pedra, papel ou tesoura: ").lower()

if player not in jogadas:
    print("Opção inválida, você deve jogar pedra, papel ou tesoura")
    player = input("Jogue pedra, papel ou tesoura: ").lower()

computador = jogadas[random.randint(0,2)]

if player == computador:
    print("Empate!")
elif player == "pedra":
    if computador == "papel":
        print(f"Computador jogou {computador}, você perdeu!")
    elif computador == "tesoura":
        print(f"Computador jogou {computador}, você ganhou!")
elif player == "papel":
    if computador == "tesoura":
        print(f"Computador jogou {computador}, você perdeu!")
    elif computador == "pedra":
        print(f"Computador jogou {computador}, você ganhou!")
elif player == "tesoura":
    if computador == "pedra":
        print(f"Computador jogou {computador}, você perdeu!")
    elif computador == "papel":
        print(f"Computador jogou {computador}, você ganhou!")