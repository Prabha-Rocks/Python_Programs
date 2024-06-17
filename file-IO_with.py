# seek()
with open('readme.txt','r') as f:
    print(type(f))
#Move to 6th byte in the file
    f.seek(10)
#Read next 5 bytes
    data = f.read(5)
    print(data)

# tell()
with open('readme.txt','r')as f:
#Read the first 10 bytes
    data=f.read(10)
#save the current_position
    current_position=f.tell()
#seek to the saved position
    f.seek(current_position)
    print(f.tell())

# truncate
with open('readme1.txt','w')as f:
    f.write('Hello World!!!')
    f.truncate(5)
with open('readme1.txt','r') as f:
    print(f.read())
