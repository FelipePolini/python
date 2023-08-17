preco = float(input("\nValor do produto: "))
qtd = int(input("\nQuantidade de produto: "))

total = preco * qtd

if qtd <= 9:
    print(f"\nDeu R$ {total:,.2f}\nVoê não possui desconto")
elif qtd >=10 and qtd <=99:
    print(f"\nDeu R$ {total:,.2f}\ncom desconto de 5% = R$ {total*0.95:,.2f}")
elif qtd >=100 and qtd <=999:
    print(f"\nDeu R$ {total:,.2f}\ncom desconto de 10% = R$ {total*0.9:,.2f} ")
elif qtd >=1000:
    print(f"\nDeu R$ {total:,.2f}\nValor com desconto de 15% = R$ {total*0.85:,.2f}")