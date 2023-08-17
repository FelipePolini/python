print ("   Bem vindo a lanchonete do senai"     )
print (            "CARDÁPIO"               )
print ("|Código|   Descrição        | Valor |")
print(" |100|   cachorro-quente     |  9,00 |")
print(" |101| cachorro-quente duplo | 11,00 |")
print(" |102|       x-egg           | 12,00 |")
print(" |103|     x-salada          | 12,00 |")
print(" |104|     x-bacon           | 14,00 |")
print(" |105|     x-tudo            | 17,00 |")
print(" |200|  refrigerante lata    | 5,00  |")
print(" |201|     chá gelado        | 4,00  |")

lista = []
total = 0

cardapio = {
    100: {"descricao": "Cachorro Quente", "valor": 9.00},
    101: {"descricao": "Cachorro Quente Duplo", "valor": 11.00},
    102: {"descricao":"X-Egg", "valor": 12.00},
    103: {"descricao":"X-Salada", "valor": 12.00},
    104: {"descricao":"X-Bacon", "valor": 14.00},
    105:{"descricao":"X-Tudo", "valor": 17.00},
    200:{"descricao":"Refri Lata", "valor": 5.00},
    201:{"descricao":"Chá Gelado", "valor": 4.00}

}

while True:
   
    codigo = int(input("\ndigite o codigo desejado: "))

    #lista.append(cardapio[codigo]['descricao'and 'valor'])
    #lista.append(cardapio[codigo]['valor'])

    while codigo not in cardapio:
        print("\ncodigo invalido")
        codigo = int(input("\ndigite o codigo desejado: "))
 
    print(f"Você pediu um(a) {cardapio[codigo]['descricao']}, {cardapio[codigo]['valor']}")
    #lista.append(codigo)


    total += cardapio[codigo]['valor']

    opcao = input("\ndeseja pedir mais alguma coisa? (S/N)").lower()
    
    if opcao == "s":
        continue
    elif opcao == "n":   
        break
print("\nSeu pedido foi: ")
for i in lista:
    print(f"\n{cardapio[codigo]['descricao'], cardapio[codigo]['valor']}")
print("\n----------------------------------------")
print(f"\nO seu pedido ficou no total de R${total}")
