while True:
    print("----Menu----")
    print("1.choose trukytnuku")
    print("2.cube")
    print("3.quit")
    a=int(input("1-3: "))
    if a == 1:
        print("choose 1.д, 2.е")
        b=int(input("1/2: "))
        if b == 1:
            print("*****")
            print(" *** ")
            print("  *")
            print("  *")
            print(" ***")
            print("*****")
        elif b == 2:
            print("*    *")
            print("**  **")
            print("******")
            print("**  **")
            print("*    *")
        else:
            print("incorrect input")
    elif a == 2:
        print("    __________")
        print("   /        /|")
        print("  /        / |")
        print(" +--------+  +")
        print(" |        | /")
        print(" |        |/")
        print(" +--------+")
    elif a == 3:
        break
    else:
        print("incorrect input")