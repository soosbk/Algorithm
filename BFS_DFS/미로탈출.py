
def solution(n, m, x, y, r, c, k):
    answer = 'impossible'

    stack=[[x,y,'',0]] #[[x,y],s,distance]
    dx=[1,0,0,-1]
    dy=[0,-1,1,0]

    while stack:
    	cx,cy,cs,cd=stack.pop()
    	if (cx,cy)==(r,c) and cd==k: return cs
    	if (cx,cy)==(r,c) and (k-cd)%2==1: continue
    	if abs(cx-r)+abs(cy-c)+cd>k: continue
    	for d in range(4):
    		nx=cx+dx[d]
    		ny=cy+dy[d]
    		nd=cd+1
	    	if nx<=0 or nx>n or ny<=0 or ny>m: continue
    		if nd+abs(nx-r)+abs(ny-c)>k: continue

    		if d==0:
    			ns=cs+'d'
    		elif d==1:
    			ns=cs+'l'
    		elif d==2:
    			ns=cs+'r'
    		else:
    			ns=cs+'u'
    		stack.append([nx,ny,ns,nd])
    		break



    return answer
