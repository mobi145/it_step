def show_even_numbers(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)

    if start % 2 != 0:
        start += 1

    for number in range(start, end + 1, 2):
        print(number)

a=int(input("a="))
b=int(input("b="))
show_even_numbers(a, b)