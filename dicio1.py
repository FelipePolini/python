itens = {
    1 : {"descricao": "capa de chuva",
        "valor": 5.00 },
    2 : {"descricao": "carrinho de brinquedo",
        "valor": 2.00}
}


while True:
    
    print("\nDigite 0 para MOSTRAR os itens da lista e SAIR")
    print("\nDigite 1 para REMOVER um item na lista")
    print("\nDigite 2 para ADICIONAR um item na lista")
    print("\nDigite 3 para ALTERAR um item na lista")

    codigo = int(input("\nDigite qual opção o senhor(A) deseja: "))

    if codigo == 0:
        break
    elif codigo == 1:
        itens.pop(int(input("\nDigite qual deseja excluir: ")))
        
    elif codigo == 2:
        adiciNum = int(input("\nDigite o número que deseja adicionar: "))
        adicionar = input("\nDigite o que deseja adicionar na descricao: ")
        adiciValor = float(input("\nDigite o valor: "))   
        
        itens[adiciNum] = {'descricao': adicionar, 'valor': adiciValor}

        if adiciNum == 1 or adiciNum == 2:
            opcao = input("\nEste código já existe, deseja digitar outro? (S/N)").lower()
            if opcao == "s":
                adiciNum = int(input("\nDigite o número que deseja adicionar: ")).lower()
                continue
            if opcao == "n":
                break

                #itens[adiciNum] = {'descricao': adicionar, 'valor': adiciValor}
                
    elif codigo == 3:
        modificar = int(input("\nQual opcção deseja modificar? "))
        if modificar in itens:
            itens.pop(modificar)
            itensLista = input("\nDigite os itens que deseja mudar: ")
            itensValor = float(input("\nDigite o valor: "))
        
            itens[modificar] = {'descricao': itensLista, 'valor': itensValor}
            

    opcao = input("\nVocê deseja fazer algo mais? (S/N)").lower()
    if opcao == "s":
        continue
    elif opcao == "n":
        break



        #itens[adiciNum] = {'descricao': adicionar, 'valor': adiciValor}
        #break
print()
print(itens)





