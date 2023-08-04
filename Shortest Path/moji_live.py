import heapq
def solution(food_times, k):
    answer = 0
    time=0
    q=[]
    if sum(food_times)<=k: 
    	return -1
    for i in range(len(food_times)):
    	heapq.heappush(q,(food_times[i],i+1))
    

    sum_value=0 # 이전단계까지 사용
    previous=0
    time=len(food_times)
    while sum_value+(q[0][0]-previous)*time<=k:
    	now=heapq.heappop(q)[0]
    	sum_value+=(now-previous)*time
    	time-=1
    	previous=now
    	

    result=sorted(q,key=lambda x:x[1])

    answer=result[(k-sum_value)%time][1]
        
    return answer
