def readSalesFile():
    salesVector = []
    file = open("VENDAS.txt")
    for s in file.readlines():
        s = s.rstrip()
        L = s.split()
        for i in range(6):
            if i < 5:
                L[i] = int(L[i])
            else:
                L[i] = float(L[i])
        salesVector.append(tuple(L))
    file.close()
    print("Reading of VENDAS.TXT ok. were read {} \ lines".format(len(salesVector)))
    return salesVector