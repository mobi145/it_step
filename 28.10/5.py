start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

if start > end:
    start, end = end, start

product = 1
count = 0

for i in range(start, end + 1):
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        count += 1

if count > 0:
    print(f"Добуток чисел, що відповідають умовам: {product}")
else:
    print("У заданому діапазоні немає чисел, які діляться на 4 і не діляться на 6.")