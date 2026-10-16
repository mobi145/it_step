a=int(input("перше число: "))
b=int(input("друге число: "))
c=int(input("третє число: "))
d=input("max або min або med: ") #med це типу середнє арифметичне
if d=="max":
    print(max(a,b,c))
elif d=="min":
    print(min(a,b,c))
elif d=="med":
    print((a+b+c)/3)
else:
    print("неправильно")