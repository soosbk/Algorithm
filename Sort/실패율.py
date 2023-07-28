def solution(N, stages):
    stages=sorted(stages)
    lst=[]
    s=len(stages)
    for i in range(1,N+1):
    	cnt=stages.count(i)
    	if s==0: lst.append((i,0))
    	else: lst.append((i,cnt/s))
    	s-=cnt


    new_s=sorted(lst,key=lambda x: -x[1])
	

    answer=[t[0] for t in new_s]

    return answer
