n=input()

left=0
right=0

for i in range(0,len(n)//2):
	left+=int(n[i])

for j in range(len(n)//2,len(n)):
	right+=int(n[j])


if left==right: print("LUCKY")
else: print("READY")
