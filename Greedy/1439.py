n=input()

result=0

s=0
b=0
now=n[0]
for i in n:
	if i==now: continue
	else:
		if now=='0':s+=1
		else:
			b+=1
		now=i


if b>s: print(b)
else: print(s)
