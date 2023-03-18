def binario(X):
    if X/2 < 1:
        if X%2 == 0:
            return '0'
        elif X%2 == 1:
            return '1'
    else:
        if X%2 == 0:
            y=X//2
            return binario(y)+'0'
        elif X%2 == 1:
            y = X // 2
            return binario(y)+'1'


valor = int(input("Valor para virar binario:"))
numBi = binario(valor)

print(valor,'em binario é',numBi)