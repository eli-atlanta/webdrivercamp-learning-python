#!/usr/bin/env python3
x = 100
y = "Learning Python is fun"
txt = "Learning Python is fun\"\' - {0} %".format(x)
print(f'{y}\"\' - {x} %')
print(txt)
print("""Learning Python is fun"'""","-",x,"%")
