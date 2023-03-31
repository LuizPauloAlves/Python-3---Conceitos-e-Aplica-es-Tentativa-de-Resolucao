def checkStockDemand():
    global product, sales, outputFile
    dictionaryStock = {}
    for codeProduct in product.keys():
        dictionaryItem = {}
        dictionaryItem['stock'] = product[codeProduct]['stock']
        dictionaryItem['minimumAmount'] = product[codeProduct]['minimumAmount']
        dictionaryItem['demand'] = 0
        dictionaryStock[codeProduct] = dictionaryItem
    for sale in sales:
        codeProduct = sale[3]
        dictionaryStock[codeProduct]['demand'] += sale[4]
    outputFile.write("-"*52 + "start of block ---\n")
    outputFile.write("need for stock in the period\n")
    outputFile.write("-"*70+"\n")
    outputFile.write(" "*9 + "Stock" + " "*14 + "Stock" + " "*4
                     + "Stock" + " "*6 + "Need\n")
    outputFile.write("Product     Start     Demand" + " "*7 +
                     "Finish      minimum   Buy\n")
    sSave = "{:<5} {:>10d} {:>10d} {:>10d} {:>10d} {:>10d}"
    for codeProduct, data in dictionaryStock.items():
        stockFinish = data['stock'] - data['demand']
        if stockFinish < 0:
            stockFinish = 0
        needBuy = data['demand'] - data['stock'] + data ['minimumAmount']
        if needBuy < 0:
            needBuy = 0
        outputFile.write(sSave.format(
            codeProduct,
            data['stock'],
            data['demand'],
            stockFinish,
            data['minimumAmount'],
            needBuy))
        outputFile.write('-'*55 + 'end of block --' +'\n\n\n')