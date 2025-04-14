from itertools import permutations
w = 'SENDMORY'
for k in permutations(range(10), len(w)):
 s, e, n, d, m, o, r, y = k
 if s == 0 or m == 0:
   continue
 send = s * 1000 + e * 100 + n * 10 + d
 more = m * 1000 + o * 100 + r * 10 + e
 money = send + more
 if money == (m * 10000 + o * 1000 + n * 100 + e * 10 + y):
   print(send,more,money)
