n=int(input())
a=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())




min_result=1e9
max_result=-1e9


def dfs(i,now):
	global min_result, max_result, add,sub,mul,div
	if i==n:
		min_result=min(now,min_result)
		max_result=max(now,max_result)

	else:
		if add>0:
			add-=1
			dfs(i+1,now+a[i])
			add+=1
		if sub>0:
			sub-=1
			dfs(i+1,now-a[i])
			sub+=1
		if mul>0:
			mul-=1
			dfs(i+1,now*a[i])
			mul+=1
		if div>0:
			div-=1
			dfs(i+1,int(now/a[i]))
			div+=1

dfs(1,a[0])

print(max_result)
print(min_result)

