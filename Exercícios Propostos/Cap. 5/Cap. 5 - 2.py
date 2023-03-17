def EPrimo(P):
    if P <= 1:
        return 'Erro' # retorna Erro se P <= 1
    elif P == 2 or P == 3: # se P é 2 retorna 1 indicando
        return 1 # que é primo
    elif P % 2 == 0: # dado que P não é dois, se ele for
        return 0 # par, então, retorna 0, não é primo
    else: # P é ímpar, então, é necessário
        raiz = P ** 0.5
        R = 1
        i = 3
        while i <= raiz and R != 0:
            R = P % i
            i+=2
        if R !=0 :
            return 1
        else:
            return R

Teste = int(input('Digite um valor:'))

for i in range(1,Teste+1):
    valor = EPrimo(i)
    if valor != 0:
        print(i,'é primo')
    else:
        print(i,"não é primo")
