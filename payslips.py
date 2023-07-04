class paySlips:
    def __init__(self,name,payment,amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = 'yes'
    
    def status(self):
        if self.payment == 'yes':
            return self.name + ' is paid ' + str(self.amount)
        else:
            return self.name + ' is not paid'
        
eugene = paySlips('Eugene','no',1000)
print(eugene.status())
eugene.pay()
print(eugene.status())