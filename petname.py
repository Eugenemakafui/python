import random

with open('petnames.txt','r') as file:
    f = file.read()
    fileList = f.split('\n')
    print(random.choice(fileList))