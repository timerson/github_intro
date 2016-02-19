def boxPrint(symbol, width, height):
    print(symbol * width)
    for  i in  range (height -2):
        print (symbol + (' ' * (len(symbol)*(width - 2))) + symbol)

    print(symbol * width)

boxPrint('***', 14, 5)
boxPrint('oxo', 4,30)

        
