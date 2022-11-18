#Writing a list
a=[34,2,1,7]
print(a)# To Print a list
#Accessing from list
print(a[1])
a.sort() #To sort in ascending order
print(a)
a.reverse()#To reverse a list,descending order
print(a)
print(max(a))# Print amx no. 34
a.append(24)# To add and element at the end
print(a)
#To Insert element at any pos
a.insert(2,67)
print(a)# To Insert Element at 2nd pos
a.remove(67) # To Remove 67 from list
print(a)
a.pop() # To Remove last Element i.e 24
print(a)
#Mutable - Can change , eg: List
#Immutable - Cannot be Changed , eg: Tuple,String
#TUPLE
tp =(1,2,3)
print(tp)
#SWAPPING TWO NUMBERS IN PYTHON
a=10
b=20
a,b = b, a # Function Specially usd in python to swap nos.
print(a,b)