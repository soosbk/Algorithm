num=int(input())

for i in range(0,num):
	s=input()
	li=s.split(" ")
	p=" ".join(reversed(li))
	print('Case #{}: {}'.format(i+1,p))
	


