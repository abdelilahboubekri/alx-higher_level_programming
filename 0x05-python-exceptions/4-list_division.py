#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(0, list_length):

        try:

            S = my_list_1[i] / my_list_2[i]

        except TypeError:
            print("wrong type")
            S = 0
        except ZeroDivisionError:
            print("division by 0")
            S = 0
        except IndexError:
            print("out of range")
            S = 0
        finally:
            new_list.append(S)
        return (new_list)
