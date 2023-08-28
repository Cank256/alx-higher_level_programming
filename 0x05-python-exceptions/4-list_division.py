#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                element1 = my_list_1[i]
                element2 = my_list_2[i]
                for element in (element1, element2):
                    if not all(isinstance(element, (int, float))):
                        print("wrong type")
                        result_list.append(0)
                    elif element2 == 0:
                        print("division by 0")
                        result_list.append(0)
                    else:
                        result = element1 / element2
                        result_list.append(result)
            except IndexError:
                print("out of range")
                result_list.append(0)
    finally:
        return result_list
