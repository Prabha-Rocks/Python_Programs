term=0
num=int(input("Enter number of terms :"))
n1,n2=0,1
if num<=0:
 print(f"Invalid Input!\nNumber of term cannot be {num}")
else:
    while term < num:
        print(n1, end =" ")
        nth=n1+n2
        n1=n2
        n2=nth
        term+=1
