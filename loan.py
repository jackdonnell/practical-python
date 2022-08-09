money_owed = float(input('How much do you owe, broke ass\n'))
apr = float(input('what is the apr\n'))
payment = float(input('what will your monthly payment be\n'))
months = int(input('Howm many months do you want to see results for\n'))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    if money_owed - payment < 0:
        print('the last payment is', money_owed)
        print('your loan was paid off in', i+1, 'months')
        break
    
    money_owed = money_owed - payment

    print('paid', payment, 'of which', interest_paid, 'was interest', end= ' ')
    print('now i owe', money_owed)