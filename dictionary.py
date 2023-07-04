sampleDict = {1: 'Coffee',2: 'Tea',3: 'Juice'}
print(sampleDict[1])
sampleDict[2]='Mint tea'
print(sampleDict)
del sampleDict[3]
sampleDict['Name']='Eugene'
print(sampleDict)
for key,value in sampleDict.items():
    print(str(key)+' '+str(value))