#!/usr/bin/env python3
x = 3.141592653589793238
y = "Learning Python is fun"
z = round(x,2)
txt = "Learning Python is fun\"\' - {0} %".format(z)
print(f'{y}\"\' - {z} %')
print(txt)
print("""Learning Python is fun"'""","-",z,"%")
print(type(x))
