num=int(input())
a=[]
for i in range(0,num):
    n=int(input())
    if(n!=0):
        a.append(n)
    else:
        if i==0:
            continue
        else:
            del(a[-1])
count=sum(a)
print(count)
