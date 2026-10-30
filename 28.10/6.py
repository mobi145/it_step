A = float(input("Введіть число A: "))
N = int(input("Введіть степінь N (ціле число): "))

result = 1

if N > 0:
    for i in range(N):
        result *= A

elif N < 0:
    for i in range(-N):
        result *= A
    result = 1 / result

print(f"{A} у степені {N} дорівнює {result}")