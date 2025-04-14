first = []
n4 = str()
for i in range (100000,999999):
    n=i
    n1=str(n)[1:]
    n2=n+1
    n2_=str(n2)[1:]
    n3=n+2
    n3_=str(n3)[1:][:-1]
    n4=n+3
    n4_=str(n4)
    if n1==n1[::-1] and n2_==n2_[::-1] and n3_==n3_[::-1] and n4_==n4_[::-1]:
        first.append(n)
print (first)
