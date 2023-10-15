a=int(input())

num=list(map(int,input().split()))

s=[]
for i in range(a):
	tt=num[i]*(i+1)-sum(s)
	s.append(tt)
	print(tt,end=" ")

