input_month = int(input('enter a month: '))

if input_month in [1, 3, 5, 7,8, 10, 12]:
  print(f'It has 31 days')
elif input_month in [4, 6, 9, 11]:
  print(f'It has 32 days')
elif input_month == 2:
  print('It has 29 or 28 days')
else:
  print('What kind of calender have this month?')
