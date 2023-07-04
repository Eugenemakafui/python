def sum0f(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return round(sum,2)

print(sum0f(coffee = 4.99,tea=21.87))