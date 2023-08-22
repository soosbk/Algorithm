def rotation(key,n):
	new_key=[[0]*n for _ in range(len(key[0]))]
	for i in range(n):
		for j in range(len(key[0])):
			new_key[n-1-j][i]=key[i][j]
	return new_key

def check(lock):
    leng=len(lock)//3
    for i in range(leng,leng*2):
        for j in range(leng,leng*2):
            if lock[i][j]!=1: return False
            
    return True

def solution(key, lock):
    answer = False
    m=len(key)
    n=len(lock)
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
    for _ in range(4):
        key=rotation(key,m)
        for i in range(n*2):
            for j in range(n*2):
                for p in range(m):
                    for q in range(m):
                        new_lock[i+p][j+q]+=key[p][q]
                if check(new_lock):
                    return True

                for p in range(m):
                    for q in range(m):
                        new_lock[i+p][j+q]-=key[p][q]
                
                
    return False



key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	

print(solution(key,lock))




# lock을 늘이고, key를 90도 돌려가며 비교하기 (4 *20)
