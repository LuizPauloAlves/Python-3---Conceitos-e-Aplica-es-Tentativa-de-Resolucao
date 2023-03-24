arq = open('calculos.txt','r')
textcalculos = arq.readlines()
textC = []
j = 0
t = 0
for textcalculos in textcalculos:
    textC.append([])
    if j == 0:
        aux = 0
        for i in range(len(textcalculos)):
            if ';' == textcalculos[i] and i != len(textcalculos):
                aux2 = textcalculos[aux:i]
                textC[j].append(aux2)
                aux = i+1
        j +=1
    else:
        aux = 0
        for i in range(len(textcalculos)):
            if ';' == textcalculos[i] and i != len(textcalculos):
                aux2 = textcalculos[aux:i]
                if 'TETO' == aux2:
                    textC[j].append(aux2)
                    t = 1
                else:
                    textC[j].append(float(aux2))
                aux = i + 1
        j += 1
print(textC)