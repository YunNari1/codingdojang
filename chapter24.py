write = str(input())



w_list = write.split()
count=0
for i in w_list:
    if i=='the':
        count+=1
print(count)