def kvadrat(a, b, c, d):
    if d == "true" or d == "t":
        for i in range(a):
            print(b * c)
    elif d == "false" or d == "f":
        print(b * c)
        for i in range(a - 2):
            print(b, " " * (c - 4), b)
        print(b * c)
    else:
        print("wrong input")


a = int(input("long="))
b = (input("sumbol="))
c = int(input("wide="))
d = (input("full? (t)true/(f)false:"))

kvadrat(a, b, c, d)