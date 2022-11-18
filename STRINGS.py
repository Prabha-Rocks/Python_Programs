#STRINGS
#To Print Reverse String
a="I Love Cookie"
print(len(a))
print(a[::-1])
print(a[-6])
#True OR FALSE
a="I Love Cookie"
print(a.isalnum()) #False Since it has space in between [Alpha Numeric]
print(a.isalpha())#False Since it has has space in between[alphabet]
print(a.endswith("Cookie"))#True Since it Ends With Cookie
print(a.endswith("Prabha"))#False since it donot end with Prabha
print(a.count("o"))# Output 3 since o is 3 times in str
print(a.upper())# Full str in caps printed
print(a.lower())#Full str in lower case printed
print(a.find("Love"))# To search for a str in the given sentence[ the begining index no of the word is printed]
print(a.replace("Cookie","Animals"))# I Lve Animals ,will be printed