input_month = int(input('enter a month: '))

if input_month < 4:
  print('Spring')
elif input_month < 7:
  print('Summer')
elif input_month < 9:
  print('Autumn')
elif input_month < 13:
  print('Winter')
else:
  print('What kind of calender have this month?')
