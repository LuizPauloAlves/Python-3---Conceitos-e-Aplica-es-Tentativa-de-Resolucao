def repeticao(L):
    NewLista = []
    for i in range(len(L)):
        add = 1
        for j in range(i+1,len(L)):
            if L[i] == L[j]:
                add +=1
        if i != 0:
            x = 0
            for k in range(0,len(NewLista),2):
                if NewLista[k] == L[i]:
                    x += 1
            if x == 0:
                    NewLista.append(L[i])
                    NewLista.append(add)
        else:
            NewLista.append(L[i])
            NewLista.append(add)
    return NewLista

Lista = [0,0,0,1,1,1,2,2,2]
print(repeticao(Lista))