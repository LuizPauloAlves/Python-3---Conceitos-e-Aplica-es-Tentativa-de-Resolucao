#Reescreva o programa do Exercício resolvido 3.2 – Sequência de
#Fibonacci fazendo a seguinte alteração: leia N que será a quantidade
#de termos a ser exibida e leia um número inteiro adicional chamado
#Prim. Essa versão do programa deverá apresentar N termos da
#sequência de Fibonacci imediatamente maiores que Prim
print('Sequência de Fibonacci\n')
# leitura do número de termos
N = 0
while N < 2:
    try:
        print('Digite N >= 2')
        N = int(input('Digite N(>1): '))
        prim = int(input('Digite algum valor: '))
        if N < 2:
            print('Digite N >= 2')
    except:
        print('O dado digitado deve ser um número inteiro.')
    A = 0
    B = 1
    print('0, 1 ', end ="")
    i = 0
    while i < N: # o laço tem que exibir N-2 termos
        C = A + B
        print(', {}'.format(C), end="") # end=”” suprime a mudança de
        A = B # linha na exibição em tela
        B = C
        if prim < C:
            i += 1
    print(".")
print('\n\nFim do Programa')