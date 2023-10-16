answer = []
def dfs(start,tickets,visited):
    lst=[]
    if False not in visited: 
        answer.append(start)
        return True
    for t in range(len(tickets)):
        if start==tickets[t][0] and visited[t]==False:
            lst.append([tickets[t][1],t])
    
    if len(lst):
        answer.append(start)
                
        lst.sort()
        for i in lst:
            end,idx=i
            visited[idx]=True
            if dfs(end,tickets,visited):
                return True
            else:
                visited[idx]=False
        answer.pop()
        return False
                
    else:
        return False
            

def solution(tickets):
    start="ICN"
    visited=[False]*len(tickets)
    dfs(start,tickets,visited)
    return answer
