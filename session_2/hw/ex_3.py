number = int(input('Enter a number have 3 digits'))
number_left = number

sum = 0
for i in range(3):
  digit= number_left % 10
  number_left = number_left // 10
  sum = sum + digit

print(f'sum of {number} is {sum}')
