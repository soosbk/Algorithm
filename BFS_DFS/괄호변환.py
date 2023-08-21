def separate(p):
	cntA=0
	cntB=0
	r=len(p)
	if p[0]=='(': cntA+=1
	else: cntB+=1

	for i in range(1,len(p)):
		if p[i]=='(': cntA+=1
		else: cntB+=1

		if cntA==cntB:
			r=i+1
			break


	return p[:r], p[r:]		


def right_str(p):
	cnt=0
	for i in range(len(p)):
		if p[i]=='(':
			cnt+=1
		else:
			if cnt==0:
				return False
			cnt-=1
		
	return True






def solution(p):
	answer=""
	if len(p)==0: 
		return ''
	u,v=separate(p)
	if right_str(u):
		answer=u+solution(v)
	else:
		answer+="("
		answer+=solution(v)
		answer+=')'
		u=list(u[1:-1])
		for i in range(len(u)):
			if u[i]=='(':
				u[i]=')'
			else:
				u[i]='('
		answer+="".join(u)
		
	return answer
