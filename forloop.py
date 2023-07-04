#for i in range(10):
#    print('Looping....', i)

fruits = ['apple','mango','banana','pineapple']
#for fruit in fruits:
#    print('I love ',fruit)

#for idx,fruit2 in enumerate(fruits):
#    print(idx,fruit2)

for fruit in fruits:
    if fruit == 'banan':
        print('I love',fruit)
else:
    print('Sorry, we dont have such fruit')


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Apple Pie':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')