# Exercise 2- Faulty Calculator
# For certain value it will give faulty answers  45*3=555 , 56+9=77 , 56/6= 4
print("Enter num1:")
num1=int(input())
print("Enter num2:")
num2=int(input())
print("Enter operator: +, *, /")
op=input()
if num1==43 and num2==3 and op=="*":
    print("555")
elif num1==56 and num2==9 and op=="+":
    print("77")
elif num1==56 and num2==6 and op=="/":
    print("4")
elif op=="+":
    print(num1 + num2)
elif op=="*":
    print(num1 * num2)
elif op=="/":
    print(num1 / num2)
else:
    print("Invalid input")
