a=int(input("Enter age:"))
if(a<18):
    print("Study!!!")
elif(a==18):
    print("u can vote,study")
elif(a>18 and a<60):
    if(a>=55 and a<60):
        print("Near to retirement")
    else:
        print("work,work")
else:
    print("Retire and rest")
