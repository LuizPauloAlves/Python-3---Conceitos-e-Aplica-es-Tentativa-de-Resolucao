def operacao(L):
    Soma = sum(L)
    media = sum(L)/len(L)
    Max = max(L)
    Min = min(L)
    tupla = (Soma, media, Max, Min)
    return tupla

lista = [0,1,2,3,4,5,6,7,8,9]
print(operacao(lista))