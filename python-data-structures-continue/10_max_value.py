#!/usr/bin/python3
def max_value(d):
    if d == dict_:
        keymax = max(zip(dict_.values(), dict_.keys()))[1]
        return keymax
    else:
        return d

if __name__=="__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")

    max_key = max_value(None)
    print(f"Max number - {max_key}")
