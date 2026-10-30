total_sum = 0
max_num = None
min_num = None

print("Вводьте числа (для виходу введіть 7):")

while True:
    num = int(input("Введіть число: "))

    if num == 7:
        print("Good bye!")
        break

    total_sum += num

    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num

if max_num is not None:
    print(f"\nСума: {total_sum}")
    print(f"Максимум: {max_num}")
    print(f"Мінімум: {min_num}")