
num="0123456789"
s=list(input())
s.sort()
print(s)
cnt=0
for i in range(len(s)):
	if s[i] in num:
		cnt+=int(s[i])
	else: break

ns="".join(s[i:])
print(ns+str(cnt))
