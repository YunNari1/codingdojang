a, b = map(int, input().split())
c=[]
for i in range(a,b+1):
    j=2**i
    c.append(j)
del c[1]
del c[-2]
print(c)