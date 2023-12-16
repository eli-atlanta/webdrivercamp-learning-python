#!/usr/bin/python3
import random
random_num = random.randint(-10000, 10000)
last_digit = int(str(random_num)[-1])
if random_num < 0:
	print(f'{random_num} - the last digit -{last_digit} is negative')
elif random_num > 0:
	print(f'{random_num} - the last digit {last_digit} is positive')
elif random_num == 0:
	print(f'{random_num} - the last digit {last_digit} is zero')
