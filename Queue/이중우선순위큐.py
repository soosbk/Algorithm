from heapq import heappush, heappop
def solution(operations):
    qmax=[]
    qmin=[]
    for operation in operations:
        if operation[0]=="I":
            heappush(qmin,int(operation[2:]))
            heappush(qmax,-int(operation[2:]))
        else:
            if qmin:
                if operation=="D -1": #최솟값
                    num=heappop(qmin)
                    qmax.remove((-1)*num)
                else:
                    num=heappop(qmax)
                    qmin.remove((-1)*num)
        
            
    if qmin:
        return [(-1)*heappop(qmax),heappop(qmin)]
    else:
        return [0,0]
