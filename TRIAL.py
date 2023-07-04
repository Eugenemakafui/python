def mul(num):
    for i in range(1,11):
        multi = num * i
        print('{multiplier} * {multiplicant} = {result}'.format(
            multiplier = num, multiplicant = i, result = num * i
        ))

def main():
    mul(5)

if __name__ == '__main__':
    main()
