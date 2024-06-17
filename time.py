import time
# print(5)
# time.sleep(7)
# print("This is printed after 7 secs of printing 5")

# t=time.localtime()
# time_date=time.strftime("Date: %d-%m-%y and Time_now- %H:%M:%S",t)
# print(time_date)

def usingWhile():
  i = 0
  while i<20000:
    i = i +1
    print(i)

def usingFor():
  for i in range(20000):
    print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)
