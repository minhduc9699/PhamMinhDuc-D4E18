import math

x = int(input('x = '))
y1 = 4 * (x**2 + 10*x * math.sqrt(x) + 3*x + 1)
y2 = (math.sin(math.pi * x**2) + math.sqrt(x** 2 + 1)) / (math.e**(2*x) + math.cos(math.pi / 4 * x))
print(f'y1 = {y1}')
print(f'y2 = {y2}')


