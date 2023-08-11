n,c=map(int,input().split())

x=[]
for _ in range(n):
	x.append(int(input()))



x.sort()
end=x[-1]-x[0]
start=1
answer=0

while start<=end:
	mid=(start+end)//2
	cnt=1
	now=x[0]
	for i in range(1,n):
		if x[i]-now>=mid:
			now=x[i]
			cnt+=1

	if cnt>=c:
		start=mid+1
		answer= mid

	else:
		end=mid-1

print(answer)
