print("Compute Number of 'a' in string")
s=input("Enter string :")
list(s)
count=0
for i in s:
 if i=="a":
    count+=1
if count==0:
    print("Not found")
else:
    print(count)