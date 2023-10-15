from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while K>scoville[0]:
        heappush(scoville,heappop(scoville)+heappop(scoville)*2)
        answer+=1
        if len(scoville)==2 and scoville[0]+2*scoville[1]<K: return -1
        if len(scoville)==1:
                if scoville[0]>=K: return answer
                else: return -1
        
        
        
    return answer
