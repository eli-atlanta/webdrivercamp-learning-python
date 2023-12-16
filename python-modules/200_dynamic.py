#!/usr/bin/python3

import sys

n = len(sys.argv)
x = n - 1
if x == 1:
	print(x, "argument.")
else:
	print(x, "arguments.")

if len(sys.argv) > 1:
	for arg in sys.argv[1:]:
		print(arg)
else:
	print('0 arguments.')
