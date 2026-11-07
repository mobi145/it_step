while True:
    print("----Menu----")
    print("1.choose trukytnuku")
    print("2.kvadrat")
    print("3.quit")
    a=int(input("1-3: "))
    if a == 1:
        print("choose 1.в, 2.г, 3.ж, 4.з")
        b=int(input("1/2/3/4: "))
        if b == 1:
            print("*****")
            print(" *** ")
            print("  *  ")
            print("")
            print("")
        elif b == 2:
            print("")
            print("")
            print("  *")
            print(" ***")
            print("*****")
        elif b == 3:
            print("*")
            print("**")
            print("***")
            print("**")
            print("*")
        elif b == 4:
            print("    *")
            print("   **")
            print("  ***")
            print("   **")
            print("    *")
        else:
            print("incorrect input")
    elif a == 2:
        print('⬛')
    elif a == 3:
        break
    else:
        print("incorrect input")