n = 5  
for i in range(1, 2*n):
    if i <= n:
        print(' ' * (n - i) + '*' * (2 * i - 1)) #upper triangle,including middle row
    else:
        print(' ' * (i - n) + '*' * (2 * (2 * n - i) - 1)) #lower triangle
