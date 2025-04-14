import math
x = int(input())
count = 0
for a in range(1, int(math.isqrt(x)) + 1):
    for b in range(a, int(math.isqrt(x)) + 1): 
        if a*a + b*b == x:
            count += 1
print(count)
