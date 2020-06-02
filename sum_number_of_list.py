def sum_numbers_of_list(abc):
    if len(abc) == 1:
        return abc[0]
    else:
        return abc[0] + sum_numbers_of_list(abc[1:])


print(sum_numbers_of_list([1,2,3,4,5]))
