from itertools import permutations # 모든 조합

n=int(input())
data=list(map(int,input().split()))
x=list(map(int,input().split()))
#덧셈, 뺄셈, 곱셈, 나눗셈
op=[]
for i in range(4):
	for j in range(x[i]): op.append(i)
candidates=list(set(permutations(op,n-1)))


min_result=1e9
max_result=-1e9

for candidate in candidates:
	now=data[0]
	for i in range(0,n-1):
		if candidate[i]==0:
			now+=data[i+1]
		elif candidate[i]==1:
			now-=data[i+1]
		elif candidate[i]==2:
			now*=data[i+1]
		else:
			now=int(now/data[i+1])

	max_result=max(max_result,now)
	min_result=min(min_result,now)

print(max_result)
print(min_result)

