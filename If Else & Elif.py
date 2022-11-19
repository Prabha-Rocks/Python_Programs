#Comparison between a and b
a=34
print("b:")
b=int(input())
if a>b:
    print("a is greater than b")
elif (a==b):
    print("value of a equals value of b")
else:
    print("a is less than b")

list=[2,6,78,5]
print(5 in list) # Instead of using if else python provides "in" and "not in" function to check conditionality
print(5 not in list)
# Ques Prac
Age= int(input("Age: "))
if (Age > 18):
    print("U can drive")
elif (Age==18):
    print("Physical Verification needed")
else:
    print("U Cannot Drive ")