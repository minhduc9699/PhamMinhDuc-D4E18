input_angles = input('Enter three angles separate by , :').split(',')

same_angle_count = 0
vertex_smaller_than_0 = 0
angles_sum = 0
for i in range(len(input_angles)):
  same_angle_count = input_angles.count(input_angles[i]) 
  angles_sum += int(input_angles[i])
  if int(input_angles[i]) <= 0:
    vertex_smaller_than_0 += 1

if angles_sum != 180 or vertex_smaller_than_0 > 1:
  print(f'you can not create triangle with these angles')
else:
  if '90' in input_angles:
    print('you can create a right triangle with these angles')
  elif same_angle_count == 3:
    print('you can create an equilateral triangle with these angles')
  elif same_angle_count == 2:
    print('you can create an isosceles triangle with these angles')
  else:
    print('you can create a triangle with these angles')
  
  

