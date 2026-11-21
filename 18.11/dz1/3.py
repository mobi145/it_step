def find_minimum(list):
    min_val = list[0]
    for num in list:
        if num < min_val:
            min_val = num
    return min_val

print(find_minimum([-4, -3, -2, -1, 0, 1, 2]))