
expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum = 0

# for i in expenses:
#     sum = sum + i

total = sum(expenses)
print('You spent $', total, ' on lunch this week', sep = '')

total = 0
expenses1 = []
num_expenses = int(input('enter # of expenses:\n'))
for i in range(num_expenses):
    expenses1.append(float(input('Enter an expense:\n')))

total = sum(expenses1)
print('You spent $', total, sep = '')
