employeeList = [{'id': 1234,'name': 'Eugene', 'department': 'Regulatory Administration\
                 '},{'id': 5678, 'name': 'Doreen', 'department': 'Finance'}]

def findEmployee(id):
    for employee in employeeList:
        if employee['id'] == id:
            return(employee)
        else:
            return('Unknown Employee')
        
print(findEmployee(1234))
