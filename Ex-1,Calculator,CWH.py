#menu driven calculator
import math
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y!=0:
        return x/y
    else:
       return "Error division by 0 undefined"
def rem(x,y):
    return x%y
def expo(x,y):
    return x**y
def floor(x,y):
    return x//y
def ceil(x):
    return math.ceil(x)
def exit_prog():
    print("Exit Program")
    return None
def main():
    operations = {'1': add,
                  '2': sub,
                  '3': mul,
                  '4': div,
                  '5': rem,
                  '6': expo,
                  '7': floor,
                  '8': ceil,
                  '9': exit
    }
    while True:#infinite loop until exit
        print("\n Menu Driven Calculator ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Division")
        print("5. Remainder")
        print("6. Exponent")
        print("7. Floor")
        print("8. Ceil")
        print("9. Exit")
        choice =input("Enter choice from 1-9:")
        if choice=='9':
            operations[choice]()
            break
        elif choice in operations:
            if choice =='8':
                x=float(input("Enter float num:"))
                result=operations[choice](x)
                print(f"ceil({x})={result}")
            else:
                x=int(input("num1(int):"))
                y=int(input("num2(int):"))
                result=operations[choice](x,y)
                if choice=='1':
                    print(f"{x}+{y}={result}")
                elif choice=='2':
                    print(f"{x}-{y}={result}")
                elif choice=='3':
                    print(f"{x}*{y}={result}")
                elif choice=='4':
                    print(f"{x}/{y}={result}")
                elif choice=='5':
                    print(f"{x}%{y}={result}")
                elif choice=='6':
                    print(f"{x}**{y}={result}")
                elif choice=='7':
                    print(f"{x}//{y}={result}")
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()