#!/usr/bin/python3
for x in range(1,100,1):

	if x % 3 == 0 and x % 5 == 0:
		print(f'FizzBuzz {x}', sep=' ', end=' ')
	elif x % 3 == 0:
		print(f'Fizz {x}', sep=' ', end=' ')
	elif x % 5 == 0:               
		print(f'Buzz {x}', sep=' ', end=' ')
	else:
		print(x, sep=' ', end=' ')
