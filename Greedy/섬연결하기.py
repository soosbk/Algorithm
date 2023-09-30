
def find_p(parents,a):
    if parents[a]!=a:
        parents[a]= find_p(parents,parents[a])
    return parents[a]
def union(parents,a,b):
    a=find_p(parents,a)
    b=find_p(parents,b)
    if a<b:
        parents[a]=parents[b]
    else:
        parents[b]=parents[a]

    return parents
            
def solution(n, costs):
    costs=sorted(costs,key=lambda x: x[2])
    parents=[i for i in range(n)]
    answer=0
    for cost in costs:
        s,e,c=cost
        if find_p(parents,s)!=find_p(parents,e):
            parents=union(parents,s,e)
            answer+=c
        
    return answer
