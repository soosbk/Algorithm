def solution(n, s):
    if s<=n-1: return [-1]
    if s%n==0: return [s//n]*n
    answer=[s//n]*n
    for i in range(s%n):
        answer[-1-i]+=1
    return answer
