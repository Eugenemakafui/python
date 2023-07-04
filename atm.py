accountBalance = 3000.00
amountWithdrawal = 0
amountDeposit = 0
accountPassword = 'eugene45'

password = input('Please enter your password to login'\
                 ' your account: ')

if(password == accountPassword):
    print('Login Successful')
    print('1. Check Balance')
    print('2. Withdrawal')
    print('3. Deposit')

    firstAction = int(input('Select action'))
    match firstAction:
        case 1:
             print('Dear customer, your balance is GHC',accountBalance)
        case 2:
            amountToWithdraw = float(input('How much do you want to withdraw? '))
            if (amountToWithdraw > accountBalance):
                print('Insufficient funds')
            else:
                accountBalance = accountBalance - amountToWithdraw
                print('GHC{} withdrawn successfully. New balance is GHC{}'.format(amountToWithdraw,accountBalance))
       

else:
    print('Incorrect Password')
