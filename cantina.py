print("       Seja Bem Vindo")
print("**********            Cardápio          *************")
print("| CÓDIGO |           Descrição          |   PREÇO    |")
print("|   100  |        Cachorro Quente       |  R$ 9,00   |")
print("|   101  |     Cachorro Quente Duplo    |  R$ 11,00  |")
print("|   102  |             X-Egg            |  R$ 12,00  |")
print("|   103  |             X-Salada         |  R$ 13,00  |")
print("|   104  |             X-Bacon          |  R$ 14,00  |")
print("|   105  |             X-Tudo           |  R$ 17,00  |")
print("|   200  |        Refrigerante Lata     |  R$ 5,00   |")
print("|   201  |            Chá Gelado        |  R$ 4,00   |")

lista = []
pedido = []
total = 0

while True:
    codigo = input("\nDigite o código do produto desejado ou 0 para sair: ")

    codigosValidos = ("0","100","101","102","103","104","105","200","201")

    while codigo not in codigosValidos:
        print("\nCódigo inválido!")
        codigo = input("\nDigite o código do produto desejado ou 0 para sair: ")

    if codigo == "100":
        lista.append("Cachorro Quente        |  R$ 9,00   |")
        valor = 9.00
        print(f"Você pediu um cachorro-quente, valor: R${valor:.2f}")
    elif codigo == "101":
        lista.append("Cachorro Quente Duplo  |  R$ 11,00  |")
        valor = 11.00
        print(f"Você pediu um cachorro-duplo, valor: R${valor:.2f}")
    elif codigo == "102":
        lista.append("X-Egg                  |  R$ 12,00  |")
        (12.00)
        valor = 12.00
        print(f"Você pediu um x-egg, valor: R${valor:.2f}")
    elif codigo == "103":
        lista.append("X-Salada               |  R$ 13,00  |")
        valor = 13.00
        print(f"Você pediu um x-salada, valor: R${valor:.2f}")
    elif codigo == "104":
        (14.00)
        lista.append("X-Bacon                |  R$ 14,00  |")
        valor = 14.00
        print(f"Você pediu um x-bacon, valor: R${valor:.2f}")
    elif codigo == "105":
        (17.00)
        lista.append("X-Tudo                 |  R$ 17,00  |")
        valor = 17.00
        print(f"Você pediu um x-tudo, valor: R${valor:.2f}")
    elif codigo == "200":
        lista.append("Refri Lata             |  R$ 5,00   |")
        (5.00)
        valor = 5.00
        print(f"Você pediu um Refri lata, valor: R${valor:.2f}")
    elif codigo == "201":
        lista.append("Chá Gelado             |  R$ 4,00   |")
        (4.00)
        valor = 4.00
        print(f"Você pediu um Chá gelado, valor: R${valor:.2f}")
    elif codigo == "0":
        break
    
    total += valor

    opcao = input("\nDeseja continuar comprando? (S/N)").lower()
    while opcao != 's' and opcao != 'n':
        print("\nOpção inválida!")
        opcao = input("\nDeseja sair? (S/N)").lower()
    
    if opcao == 'n':
        break

print("\nSeu pedido foi: ")
for i in lista:
    print(f"\n{i}")
print("\n---------------------------------------")
print(f"\nTotal da compra        |  R${total:.2f}    |")
