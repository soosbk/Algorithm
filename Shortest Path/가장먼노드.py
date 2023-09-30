from collections import deque
def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    distance=[0]*(n+1)
    check=[False]*(n+1)
    check[1]=True
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    stack=deque([[idx,1] for idx in graph[1] ])
    while stack:
        idx,time=stack.popleft()
        if check[idx]==True: 
            continue
        distance[idx]=time
        check[idx]=True
        for i in graph[idx]:
            stack.append([i,time+1])
    m=max(distance)
    
    return distance.count(m)
