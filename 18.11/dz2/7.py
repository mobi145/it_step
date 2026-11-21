def power_elements(numbers, power):
    result = []
    for num in numbers:
        result.append(num ** power)
    return result
print(power_elements([1, 2, 3, 4, 5], 3))