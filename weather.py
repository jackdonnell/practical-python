from operator import truediv


temp = 75
forecast = 'rain'
if temp < 80 or temp > 60:
    print('go outside')
else:
    print('stay inside')

if temp < 80 and forecast != 'rain':
    print('go outside')

raining = True
if not raining:
    print('go outside')
