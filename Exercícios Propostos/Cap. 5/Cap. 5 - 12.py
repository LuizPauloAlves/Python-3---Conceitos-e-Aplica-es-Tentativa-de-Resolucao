def fibo(Q):
    L = [0,1]
    if Q < 1 :
        return 'Erro'
    elif Q == 1 :
        return 0
    elif Q == 2:
        return L
    else:
        for i in range(Q-2):
            L.append(L[i]+L[i+1])
        return L

Numero = int(input("Digite um numero:"))
print(fibo(Numero))