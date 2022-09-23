num = int(input())

for i in range(num):
    for j in reversed(range(num)):
        if i<j:
            print(" ", end='')
        else:
            print('*', end='')
    for j in range(num):
        if i>j:
            print("*",end='')
        else:
            print(" ", end='')
    print("\n",end='')