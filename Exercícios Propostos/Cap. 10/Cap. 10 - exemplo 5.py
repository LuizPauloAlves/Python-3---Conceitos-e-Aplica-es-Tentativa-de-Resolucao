def showLine(msg, size = 0, align = '^'):
    edge = (widthScreen - size - 2) // 2
    sfmt = '{:'+ align + str(size) + '}'
    print('-'*edge,sfmt.format(msg),'-'*edge)

def stop(msg, size = 64):
    if msg != '':
        showLine(msg, size)
    input()

def topScreen(msg = ''):
    print('\n'*2, '-' * widthScreen, sep = '')
    showLine('Tournament Program', 40, '^')
    if msg != '':
        showLine(msg, 40, '^')
    print('-'*widthScreen)