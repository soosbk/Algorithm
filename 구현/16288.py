n,k=map(int,input().split())
lst=list(map(int,input().split()))

idx=[0]*k
n=False
for l in lst:
	n=False
	for i in range(k):
		if idx[i]<l:
			idx[i]=l
			n=True
			break
	if n==False:
		break


if n: print("YES\n")
else: print("NO\n")

