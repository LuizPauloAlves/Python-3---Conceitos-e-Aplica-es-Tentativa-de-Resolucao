i = 0
V = []
while i == 0:
    Min = int(input("Digite um valor para min: "))
    Max = int(input("Digite um valor para max: "))
    if Max > Min:
        i = 1
while Max >= Min:
    if Min % 7 == 0:
        V.append(Min)
    Min +=1
print(V)