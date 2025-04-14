n = int(input())
if n<2:
    print(1)
else:
    for i in range(2, n+1):
        if n%i==0:
            print(i)
            break
