from collections import deque
def solution(bridge_length, weight, truck_weights):
    if len(truck_weights)==1: return bridge_length+1
    answer = 1
    nw=truck_weights[0]
    bridge=deque([truck_weights[0]])
    for t in truck_weights[1:]:
        if len(bridge)==bridge_length: 
            nw-=bridge.popleft()
        while nw+t>weight:
            while len(bridge)<bridge_length:
                bridge.append(0)
                answer+=1
            nw-=bridge.popleft()
        nw+=t    
        bridge.append(t)
        answer+=1
        
            
    return answer+bridge_length
