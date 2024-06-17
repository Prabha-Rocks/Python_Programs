f=open('readme.txt','r')
text=f.read()
print(text)
f.close()

f=open('readme.txt','w')
text=f.write("Hello from Python!!")
print(text)
f.close()

f=open('readme.txt','a')
text=f.write("\nI am learning python")
print(text)
f.close()

f=open('readme.txt','rb')
text=f.read()
print(text)
f.close()

with open ('readme.txt','a') as f:
    f.write("\nName of my Cockateil is Nimbu")