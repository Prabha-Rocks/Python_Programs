num=float(input("Enter number to compute root:"))
sq=num**0.5
if num>=0:
 sq = num ** 0.5
 print(f"Square root is : {sq}")
else:
 sq=(-num)**0.5
 print(f"Square root is :{sq}i (here i represent complex)")
