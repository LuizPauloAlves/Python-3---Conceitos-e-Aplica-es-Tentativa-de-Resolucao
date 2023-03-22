def EPrimo(P):
    if P <= 1:
        return 'Erro'
    elif P == 2:
        return 1
    elif P % 2 == 0:
        return 0
    else:
        raiz = P ** 0.5
        R = 1
        i = 3
        while i <= raiz and R != 0:
            R = P % i
            i += 2
        return R
arq = open("Primos.txt",'w')
N = int(input("Digite um numero para ver os primos até ele:"))
for i in range(2,N+1):
    if EPrimo(i) != 0:
        n = str(i)+' é primo\n'
        arq.write(n)