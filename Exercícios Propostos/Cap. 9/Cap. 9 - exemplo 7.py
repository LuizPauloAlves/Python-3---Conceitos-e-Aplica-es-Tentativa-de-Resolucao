import datetime
from random import radiant

def showPresentation():
    print('\nBacklog Order Generator')
    print('-'*40)
    print('Data needed for this programa')
    print('   - period start date')
    print('   - period end date')
    print('   - amount of sales per day')
    print('   - file PRODUTOS.TXT available')
    print('\n')
    print(' This program create a file VENDAS.TXT')
    print('-'*40)

def convertDate(d):
    d = d.split('/')
    date = datetime.date(int(d[2]), int(d[1]), int(d[0]))
    return date

def getInputs():
    s = input("Enter start date(format: dd/mm/yyyy):")
    start = convertDate(s)
    s = input("Enter end date (format: dd/mm/yyyy:")
    end = convertDate(s)
    q = int(input("Enter amount of sales per day:"))
    return start, end, q

def readFileProduct():
    dictionaryProduct = {}
    file = open("PRODUTOS.txt")
    for S in file.readlines():
        S = S.rstrip()
        L = S.split(";")
        code = int(L[0])
        dictionaryItem = {}
        dictionaryItem['stock'] = int(L[1])
        dictionaryItem['minimumAmount'] = int(L[2])
        dictionaryItem['unitPrice'] = float(L[3])
        dictionaryItem['margin'] = float(L[4])
        dictionaryProduct[code] = dictionaryItem
    file.close()
    print("Reading of PRODUTOS.TXT ok. were read {} Lines".format(len(dictionaryProduct)))
    return dictionaryProduct

def generateSalesAmount():
    global product
    raffle = radiant(1,100)
    if raffle <= 60:
        q = radiant(1,10)
    elif raffle <= 85:
        q = radiant(11,25)
    else:
        q = radiant(26,400)
    return q

def generateUnitPriceSale(codeProduct):
    global product
    priceBuy = product[codeProduct]['unitPrice']
    margin = product[codeProduct]['margin'] / 100
    range = radiant(0,10) / 100
    priceSale = priceBuy * (1 + margin + range)
    return priceSale

def generateDataDay(day, salesAmount):
    global product, file
    L = list(product.keys())
    for x in range(salesAmount):
        iproduct = radiant(0, len(product)-1)
        codeProduct = L[iproduct]
        amountItem = generateSalesAmount(codeProduct)
        unitPrice = generateUnitPriceSale(codeProduct)
        a = str(day.year)+';'+str(day.month)+';'+str(day.day)
        a = a + ';' + str(codeProduct)
        a = a + ';' + '{:.2f}'.format(unitPrice)
        a = a + '\n'
        file.write(a)

showPresentation()
dateStart, dateEnd, amount = getInputs()
product = readFileProduct()
file = open("VENDAS.txt",'w',encoding='UTF-8')
oneDay = datetime.timedelta(days=1)
counter = dateStart
while counter <= dateEnd:
    if counter.weekday() < 5:
        generateDataDay(counter, amount)
    counter = counter + oneDay
file.close()
print("\nthe data file was successfully generated")
print("\n\nProgram end")