input_year = int(input('Enter a year: '))

if not input_year % 4 == 0:
  if not input_year % 100 == 0:
    if not input_year % 400 == 0:
      print(f'{input_year} is not a leap year, it has 365 days')
else:
  print(f'{input_year} is a leap year, it has 366 days')
  
