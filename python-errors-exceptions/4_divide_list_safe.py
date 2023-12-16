#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):
    result_list = []
    for x in range(0, list_len):
        division_result = 0
        try:
            division_result = list_1[x] / list_2[x]
        except TypeError:
            print(f"wrong type")
        except ZeroDivisionError:
            print(f"division by zero")
        except IndexError:
            print(f"out of range")
        finally:
            result_list.append(division_result)
    return result_list

if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)