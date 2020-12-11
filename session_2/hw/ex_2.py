total_money = int(input('Enter your desire money'))
money_left = total_money

total_100k = money_left // 100000
money_left = money_left - total_100k * 100000

total_50k = money_left // 50000
money_left = money_left - total_50k * 50000

total_20k = money_left // 20000
money_left = money_left - total_20k * 20000

total_10k = money_left // 10000
money_left = money_left - total_10k * 10000

print(f'With {total_money} you have {total_100k} 100k, {total_50k} 50k, {total_20k} 20k, {total_10k} 10k')
