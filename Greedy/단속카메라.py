def solution(routes):
    answer = 0
    routes=sorted(routes, key=lambda x: (x[1],x[0]))
    time=-30001
    
    for r in routes:
        s,e=r
        if s<=time:
            continue
        else:
            time=e
            answer+=1
    return answer
