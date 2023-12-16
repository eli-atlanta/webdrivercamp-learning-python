#!/usr/bin/python3
def calc_weight(list_=[]):
    if len(list_) == 0:
        return 0
    else:
        x = 0
        y = 0
        for i in list_:
            a, b = i
            x += a * b
            y += b
        return x / y

            
if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
