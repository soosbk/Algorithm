def solution(n, lost, reserve):
    answer = 0
    num=[0]*(n+2)
    for i in lost:
        num[i]-=1
    for i in reserve:
        num[i]+=1
    for i in range(1,n+1):
        if num[i]==-1:
            if num[i-1]==1: 
                num[i-1]-=1
                num[i]+=1
            elif num[i+1]==1:
                num[i+1]-=1
                num[i]+=1
    
        
    return n-num.count(-1)
