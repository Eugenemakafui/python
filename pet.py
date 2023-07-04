"""with open('petnames.txt','r') as file:
    data = file.read()
    fileList = data.split('\n')
    print(fileList)"""

with open('petnames.txt','r') as file:
    data = file.read()
    fileList = data.split('\n')
    sum = 0
    for i in fileList:
        sum+=int(i)
    print(sum)
