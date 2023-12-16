#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]

print(my_list)

tuple1 = tuple(my_list)

def output():
    for i in tuple1:
        if i % 2 == 0:
            print("True")
        else:
            print("False")

output()
