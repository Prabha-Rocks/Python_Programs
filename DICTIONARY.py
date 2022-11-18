# DICTIONARY IS NOTHING BUT KEY VALUE PAIRS
d1 = {}
#Print Dictionary Datatype
print(type(d1))
# Entering and accessing values from a dictionary
d={"Fish":"Water","Food":"Roti","Fruits":{"A":"Apple","B":"Mango"}}
print(d)# To Print Full Dictionary
print(d["Fish"])# To Access value stored in fish i.e Water
# To Add a new value to a dictionary
d["Prabha"]="Cookie" # TO ADD AN ELEMENT IN THE DICTIONARY AT THE END
print(d)
# TO REMOVE AN ELE FROM DICTIONARY we use (del) Function
del d["Prabha"]
print(d)
# TO copy "d" dictionary into d3
d3 = d
d.copy() # .copy() function is used to copy a shallow value of the original value
del d["Fish"]
print(d)
print(d.items())# USED TO PRINT ALL THE DICTIONARY ITEMS
print(d.keys())# ONly the Key elements(index) of dictionary are printed
