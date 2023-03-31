# Execution start point
showPresentation()
product = readProductsFile()
sales = readSalesFile()
#below open the output file
outputFile = open("APURA.txt", "w", encoding="UTF-8")
checkStockDemand()
checkTotalsPerProduct()
outputFile.close()
print("\n\nEnd of program")