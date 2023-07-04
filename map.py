menu = ['coffee','capuccino','espresso','juice']

def getMenu(coffee):
    if coffee[0] == 'c':
        return coffee
    
mapCoffee = map(getMenu,menu)
for x in mapCoffee:
    print(x)

filterCoffee = filter(getMenu,menu)
for y in filterCoffee:
    print(y)