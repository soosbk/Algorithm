h,w,n,m=map(int,input().split())

r=h//(n+1)
if h%(n+1):
    r+=1

c=w//(m+1)


if w%(m+1): c+=1

print(r*c)
