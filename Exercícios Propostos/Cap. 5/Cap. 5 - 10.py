def repeticao(L,L2):
    NewLista = []
    for i in range(len(L)):
        if i != 0:
            x = 0
            for k in range(len(NewLista)):
                if NewLista[k] == L[i]:
                    x += 1
            if x == 0:
                    NewLista.append(L[i])
        else:
            NewLista.append(L[i])
    for j in range(len(L2)):
        ok = 0
        for n in range(len(NewLista)):
            if L2[j] == NewLista[n]:
                ok += 1
        if ok != 0:
            NewLista.remove(L2[j])
    return NewLista

Lista = [0,0,0,1,1,1,2,2,2,3,2,4,5,3,4,2,1,0,1]
Lista2 = [0,1,2,3,0,1,2,3]
print(repeticao(Lista,Lista2))