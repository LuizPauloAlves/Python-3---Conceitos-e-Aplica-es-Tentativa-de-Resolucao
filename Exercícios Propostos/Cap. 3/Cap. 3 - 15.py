max = int(input("Informe o valor Maximo:"))
min = int(input("Informe o valor Minimo:"))
if max < min:
    max, min = min, max   #faz a troca de posição entre os max e min
    print("Os valores de maximo e minimo foram trocados de posição")
while min <= max:
    if min % 5 == 0:
        print("{} ".format(min),end="")
    min +=1