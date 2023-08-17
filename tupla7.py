tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9,10)

for i in range(0,len(tupla1),1):
    print(f"{tupla1[i]} x {tupla2[i]} = {tupla1[i] * tupla2[i]}")