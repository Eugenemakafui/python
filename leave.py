class Employee:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last

class password(Employee):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password = password

class leave(Employee):
    def requestLeave(self,days):
        return 'May I take a leave for ' +str(days)+ ' days'
    
eugene = Employee('Eugene','A')
print(eugene.requestLeave(3))
