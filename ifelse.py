billTotal = 150
billDiscount1 = 10
billDiscount2 = 20

if (billTotal>100 and billTotal<200):
    print('Bill is greater than 100')
    billTotal = billTotal - billDiscount1

elif billTotal > 200:
    print('Bill is greater than 200')
    billTotal = billTotal - billDiscount2

else:
    print('Bill is less than 100')

print(f'Total bill =${billTotal}')