def sumOf(a,b):
    return a/b
try:
    print(sumOf(2,0))
#except Exception as e:
    #print('Something went wrong',e)
except ZeroDivisionError as e:
    print(e,'Cannot divide by zero')
    #Finds actual exception
    print(e.__class__)