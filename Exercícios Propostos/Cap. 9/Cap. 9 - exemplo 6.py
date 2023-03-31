def checkTotalsPerProduct():
    global product, sales, outputFile
    dictionaryTotals = {}
    for codeProduct in product.keys():
        dictionaryItem = {}
        dictionaryItem['totalOrder'] = 0
        dictionaryItem['totalAmount'] = 0
        dictionaryTotals[codeProduct] =dictionaryItem
    for sale in sales:
        codeProduct = sale[3]
        dictionaryTotals[codeProduct]['totalOrder'] += sale[4] * sale[5]
        dictionaryTotals[codeProduct]['totalAmount'] += sale[4]
    outputFile.write('-'*55 + 'start of block-\n')
    outputFile.write("Total backlog orders")
    outputFile.write('-'*70 + '\n')
    outputFile.write('Product     totalAmount    Amount    '+
                     'AvgPrice     AvgCost    AvgMargin\n')
    ssave = "{:<5} {:>11.2f} {:>8d} {:>10.2f} {:>10.2f} \ {:>10.1f}%\n"
    totalSale = 0
    for codeProduct, data in dictionaryTotals.items():
        try:
            totalSale += dados['totalOrder']
            AvgPrice = dados['totalOrder'] / dados['totalAmount']
            profit = (AvgPrice / dados['unitPrice'] - 1)* 100
        except:
            AvgPrice = profit = 0
        outputFile.write(ssave.format(
            codeProduct,
            data['totalOrder'],
            data['totalAmount'],
            AvgPrice,
            product[codeProduct]['unitPrice'],
            profit))
        outputFile.write("-"*70 + '\n')
        outputFile.write("Total {:>11.2f}\n".format(totalSale))
        outputFile.write("-"*55 + "end of block---\n\n\n")