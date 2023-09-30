from collections import deque
def solution(people, limit):
    answer = 0
    q=deque(sorted(people))
    
    while q:
        a=q.pop()
        if len(q)==0:
            return answer+1
        if q[0]<=limit-a:
            q.popleft()
        answer+=1
        
    return answer
