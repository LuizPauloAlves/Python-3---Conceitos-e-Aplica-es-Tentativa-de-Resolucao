n = int(input("valor > "))
lista = []
numero, i = 1 , 1
#O primiro valor pode ser qualquer um, ja que a lista esta vazia
lista.append(int(input("digite o valor para a posição {}>".format(numero))))
#agora que ja tem 1 valor tem que verificar os demais
while i < n:
    numero = int(input("digite o valor para a posição {}>".format(i+1)))
    #verificar se o numero esta dentro do vetor
    conf, j = 0, 0
    #inicia no primeiro item do vetor até o ulmito iten antes deste
    while j < i:
        #se o numero for igual ao da posiçao atual da lista e conf = 0
        #atribui o valor != de 0 para conf para notificar que o valor ja foi atribuido
        if conf == 0 and lista[j] == numero:
            conf = 1
        j += 1
    #caso o conf = 0 entao então nenhum, numero nas posições anteriores é igual
    if conf == 0:
        #adiciona o valor para o ultimo da lista e vai para o proximo
        lista.append(numero)
        i += 1
    #caso o conf != 0 então pedesse o novo numero para a posição esta posição
print(lista)