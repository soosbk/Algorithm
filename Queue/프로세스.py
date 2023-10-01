from collections import deque
def solution(priorities, location):
    answer = 1
    q=deque([[i,priorities[i]] for i in range(len(priorities))])
    p=deque(sorted(priorities,reverse=True))
    while True:
        idx,ps=q.popleft()
        if ps==p[0]:
            if idx==location:
                return answer
            else:
                p.popleft()
                answer+=1
        else:
            q.append([idx,ps])    
            
        
            
    return answer
