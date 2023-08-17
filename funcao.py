'''def soma():
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))    
    return soma()

soma()
print(f"Resultado = {a + b}")'''

def adicao(a,b):
    somaMais = a + b
    return somaMais

def subtracao(a,b):
    somaMenos = a - b
    return somaMenos

def divisao(a,b):
    somaDiv = a / b
    return somaDiv

def multiplicacao(a,b):
    somaVezes = a * b
    return somaVezes

def valida(x):
    while True:        
        try:
            x = float(x)
            break
        except:
            x = input("\nDigite um número: ")
            continue
    return x


def calculo():
    while True:    

        x = input("\nDigite um número: ")
        x = valida(x)
        y = input("\nDigite mais um número: ")
        y = valida(y)

        op = input("\nDigite a operação que deseja: ( /  ) ( + ) ( - ) ( x ): ")
        if op == "+":
            print(adicao(x,y))
            resultado = (a,b)
            break
        if op == "/" :
            if op == 0:
                print("\nImpossivel dividir por 0")
            else:
                print(divisao(x,y))
            break
        if  op == "-" :
            print(subtracao(x,y))
            break
        if  op == "x":
            print(multiplicacao(x,y))
            break
        else:
            print("\nOperador digitado inválido")
            continue

#print(f"{x} {op} {y} = {calculo()}")
calculo(resultado)

