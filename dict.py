menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

order = ['espresso','cake','soup']

for i in order:
    sum = 0
    if i == 'espresso':
        sum += 1.99
    elif i == 'cake':
        sum += 2.79
    else:
        sum += 4.5
print(sum)

