n = int(input())
m = 0
for i in range(n + 1):
    for j in range(i, n + 1):
        m += i + j
print(m)
