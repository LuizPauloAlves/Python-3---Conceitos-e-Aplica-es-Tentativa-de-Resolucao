l1 = int(input("Lado um do triangulo:"))
l2 = int(input("Lado dois do triangulo:"))
l3 = int(input("Lado treis do triangulo:"))
if l1 == l2 or l2 == l3 or l1 == l3:   #verifica se é tem dois lados iguais
    if l1 == l2 and l2 == l3:   #verifica se tem os 3 lados iguais
        print("Triangulo equilatero")
    else:   #caso nao tenha os 3 lados iguais encontar o maior lado
        if l1 > l2:   #L1 como maior lado, considerando q l2 = l3
            if (l2 + l3) > l1:   #ou 2 * l2
                print("Triangulo isoceles")
            else:
                print("não é um triangulo")
        elif l2 > l1:   #L2 como maior lado, considera que l1 = l3
            if (l1 + l3) > l2:   #ou 2 * l1
                print("Triangulo isoceles")
            else:
                print("não é um triangulo")
        else:    #como só sobrou o l1 = l2, e nao é um triangulo equilatero, logo l3 é o maior lado
            if (l2 + l1) > l3:   #ou 2 * l2
                print("Triangulo isoceles")
            else:
                print("não é um triangulo")
elif l1 > l2 and l1 > l3:
    if (l2 + l3) > l1:
        print("Triangulo escaleno")
    else:
        print("não é um triangulo")
elif l2 > l1 and l2 > l3:
    if (l1 + l3) > l2:
        print("Triangulo escaleno")
    else:
        print("não é um triangulo")
else:
    if (l2 + l1) > l3:
        print("Triangulo escaleno")
    else:
        print("não é um triangulo")