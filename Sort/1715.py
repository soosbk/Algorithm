import heapq

n=int(input())
card=[]
for _ in range(n):
	heapq.heappush(card,int(input()))

total=0

while len(card)!=1:
	c=heapq.heappop(card)+heapq.heappop(card)
	total+=c
	heapq.heappush(card,c)
	
	

print(total)
