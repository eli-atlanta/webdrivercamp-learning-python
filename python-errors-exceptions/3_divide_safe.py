#!/usr/bin/python3
def divide_safe(a, b):
    y = 0
    try:
        y = a / b
    except:
        y = None
    finally:
        print(f"Result: {y}")
    return y

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")