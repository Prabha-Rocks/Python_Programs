a = int(input("Enter a num:"))
match a:
    case _ if a < 0:
        print("Negative No.")
    case _ if a % 2 != 0:
        print("Odd No.")
    case _ if a % 2 == 0:
        print("Even No.")
    case _:
        print("default")
