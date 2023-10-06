def solution(n, computers):
    t=1
    checklist=[-1]*n
    for i in range(n):
        if checklist[i]>-1: continue
        stack=[[i,t]]
        while stack:
            p,t=stack.pop()
            checklist[p]=t
            for i in range(n):
                if computers[p][i]==1 and checklist[i]==-1:
                        stack.append([i,t])
                        
        t+=1
        
    return max(checklist)

