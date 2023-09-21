import math
def turn(n,k):
    lst=[]
    while n>=1:
        lst.append(str(n%k))
        n//=k
        
    a="".join(reversed(lst))
    return a

        
def is_prime(stream):
    if stream==1:
        return False
    for i in range(2,int(math.sqrt(stream))+1):
        if stream%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    stream=turn(n,k)
    cnt=stream.count('0')
    if cnt==0:
        if is_prime(int(stream)):
            return 1
        return 0
    
    new_stream=stream.split("0")
    for s in new_stream:
        if s!="" and is_prime(int(s)):
            answer+=1

    return answer
