from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    if sum(works)<=n: return 0
    q=[]
    for w in works:
        heappush(q, (-1)*w)
    while n>0:
        t=heappop(q)
        t+=1
        heappush(q,t)
        n-=1
    for i in q:
        answer+=i**2
    return answer
