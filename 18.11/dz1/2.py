def multiply_elements(list):
    product = 1
    for num in list:
        product *= num
    return product
print(multiply_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))