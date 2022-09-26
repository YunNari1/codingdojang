a, b = map(int,input().split())
A=set()
B=set()
for i in range(1,a+1):
    if a%i==0:
        A|={i}
for j in range(1,b+1):
    if b%j==0:
        B|={j}

divisor = A&B

result=0
if type(divisor)==set:
    result =sum(divisor)

print(result)
