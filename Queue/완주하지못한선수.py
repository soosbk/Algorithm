from collections import deque
def solution(participant, completion):
    pa=deque(sorted(participant))
    completion.sort()
    
    for c in completion:
        p=pa.popleft()
        if c!=p:
            return p
    
    return pa.popleft()
