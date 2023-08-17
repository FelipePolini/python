a = int(input("\nDigite qual tabuada deseja calcular: "))

for a in range(0,11,1):
    #print(f"{a} x {i} = {a*i} ")
    for i in range(0,11):
        print(f"\n{a} x {i} = {a*i}")