from itertools import combinations # 모든 조합

n,m=map(int,input().split())
array=[]
chickens=[]
homes=[]
d=[]
for i in range(n):
	array.append(list(map(int,input().split())))
	for j in range(n):
		if array[i][j]==1:
			homes.append((i,j))
		elif array[i][j]==2:
			chickens.append((i,j))

candidates=list(combinations(chickens,m))


def get_sum(candidate):
	result=0

	for hx,hy in homes:
		temp=1e9
		for cx,cy in candidate:
			temp=min(temp,abs(hx-cx)+abs(hy-cy))

		result+=temp
	return result

result=1e9
for candidate in candidates:
	result=min(result,get_sum(candidate))


print(result)
