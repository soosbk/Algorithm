n=int(input())
dp=[0]*n
dp[0]=1


i2,i3,i5=0,0,0
nex2,nex3,nex5=2,3,5

for i in range(1,n):
	dp[i]=min(nex2,nex3,nex5)


	if dp[i]==nex2:
		i2+=1
		nex2=dp[i2]*2
		

	if dp[i]==nex3:
		i3+=1
		nex3=dp[i3]*3

	if dp[i]==nex5:
		i5+=1
		nex5=dp[i5]*5


print(dp[-1])
