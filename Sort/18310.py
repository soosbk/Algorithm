n=int(input())

position=list(map(int,input().split()))
position.sort()

if len(position)%2==1:
	print(position[n//2])

else:
	first=n//2-1
	second=n//2

	s1=0
	for i in range(first):
		s1+=(position[first]-position[i])
	for i in range(first,n):
		s1+=(position[i]-position[first])

	s2=0

	for i in range(second):
		s2+=(position[second]-position[i])

	for i in range(second,n):
		s2+=(position[i]-position[second])
	
	if s1<=s2: print(position[first])
	else: print(position[second])
