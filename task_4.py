number = 0
n = int(input())
while n>0:
    if n % 2 == 0 and n>=4:
        number+=1
    n = int(input())
print(number)
