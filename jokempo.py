print("\nJogue PEDRA, PAPEL ou TESOURA\n")
jog1 = input(f"Jogador 1 :  ").upper()
jog2 = input(f"\nJogador 2 :   ").upper()


if jog1 == "pedra" and jog2 == "tesoura" or jog1 == "papel" and jog2 == "pedra" or jog1 == "tesoura" and jog2 == "papel":
    print("\nJogador 1 ganhou!!")

elif jog2 == "pedra" and jog1 == "tesoura" or jog2 == "papel" and jog1 == "pedra" or jog2 == "tesoura" and jog1 == "papel":
    print("\nJogador 2 ganhou!!")

elif jog1 == jog2:
    print("\nA partida deu empate!!")

else:
    print("\nJogada Inválida")