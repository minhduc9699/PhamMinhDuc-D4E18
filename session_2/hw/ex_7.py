numbers = input('Enter three numbers separate by , :"').split(',')

for i in range(len(numbers)):
  min_index = i
  for j in range(i+1, len(numbers)):
    if int(numbers[j]) < int(numbers[min_index]):
      min_index = j

  temp = numbers[i]
  numbers[i] = numbers[min_index]
  numbers[min_index] = temp

for i in range(len(numbers)):
  print(numbers[i])

  


