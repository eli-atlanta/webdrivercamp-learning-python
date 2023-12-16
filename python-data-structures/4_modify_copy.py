#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
list_2 = list_.copy()

index = 1
if index in range(0,4):
	element_to_replace = 5
	list_2[index] = element_to_replace

	print('Copy:', list_2) 

else:
	print('Copy:', list_2)


print('Original:', list_)
