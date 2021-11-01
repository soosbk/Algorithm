from collections import Counter

num=int(input())
count=0
dic_li=[]
for i in range(0,num):
	st=input()
	li=dict(Counter(list(st)))
	sorted(li.items())
	
	if li in dic_li: pass
	else: 
		dic_li.append(li)
		count+=1

print(count)
