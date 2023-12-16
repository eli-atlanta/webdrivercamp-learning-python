#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

chars_to_remove = ['a', 'A']

result = ''

for char in string:
	if char not in chars_to_remove:
		result += char

print(result)
	
