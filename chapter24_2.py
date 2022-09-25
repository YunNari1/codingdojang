price = str(input())
list_price2 = price.split(';')
list_price = list(map(int,list_price2))

for j in range(0, len(list_price)-1):
    for i in range(j+1,len(list_price)):
        if list_price[j]<list_price[i]:
            remember=list_price[j]
            list_price[j]=list_price[i]
            list_price[i]=remember
for k in list_price:
    print('%9s'%format(k,','))

