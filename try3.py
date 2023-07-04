names = ['Eugene','Makafui','Eugene']

def fet(acc):
    if acc[0] == 'E':
        return acc
    
match = filter(fet,names)
lisy = [x for x in match]
print(lisy)