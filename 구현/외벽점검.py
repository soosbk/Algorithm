import copy
from itertools import permutations
      

def solution(n, weak, dist):
	answer=len(dist)+1
	length=len(weak)
	for i in range(len(weak)):
		weak.append(weak[i]+n)
	

	for start in range(length):
		for lst in permutations(dist,len(dist)):
			i=1
			end=weak[start]+lst[i-1]
			for now in range(start,start+length):
				if end<weak[now]:
					i+=1
					if i>len(dist):
						break
					end=weak[now]+lst[i-1]
			answer=min(answer,i)
	if answer>len(dist): return -1
	return answer
