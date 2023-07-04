class myClass:
    def getAge(age):
        if age >= 18:
            print("You're {}. You are legible voter".format(age))
        else:
            print('You are not allowed to vote')

age = int(input('Please enter your age!: '))
myClass.getAge(age)