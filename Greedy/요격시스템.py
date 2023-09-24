def solution(targets):
    answer = 0
    targets=sorted(targets,key=lambda x: (x[1],x[0]))
    i=0
    while i<len(targets):
    	s,e=targets[i]
    	answer+=1
    	i+=1
    	while i <len(targets):
    		if targets[i][0]< e:
    			i+=1
    		else:
    			break
    		



    return answer
