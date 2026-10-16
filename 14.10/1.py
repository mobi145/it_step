a=int(input("перше число: "))
b=int(input("друге число: "))
c=int(input("третє число: "))
d=input("+ або *: ")
if d=="+":
    print(a+b+c)
elif d=="*":
    print(a*b*c)
else:
    print(f"писать треба + або * а не {d}")