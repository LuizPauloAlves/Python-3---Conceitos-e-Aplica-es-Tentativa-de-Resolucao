def readProductFile():
    dictionaryProduct = {}
    file  = open("PRODUTOS.txt")
    for S in file.readlines():
        S = S.rstrip()
        L = S.split(";")
        code = int(L[0])
        dictionaryItem = {}
        dictionaryItem["stock"] = int(L[1])
        dictionaryItem["minimumAmount"] = int(L[2])
        dictionaryItem["unitPrice"] = float(L[3])
        dictionaryItem["margin"] = float(L[4])
        dictionaryProduct[code] = dictionaryItem
        file.close()
        print("Reading of PRODUTOS.TXT ok. were read {} \ lines".format(len(dictionaryProduct)))
        return dictionaryProduct