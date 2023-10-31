

def mul(lst):
    answer=1
    for l in lst:
        answer*=(l+1)
        
    return answer-1

def solution(clothes):
    closet={}
    for c in clothes:
        if c[1] not in closet:
            closet[c[1]]=[c[0]]
        else:
            closet[c[1]].append(c[0])
    num=[]
    for k in closet:
        num.append(len(closet[k]))
    
    answer=mul(num)
      
        
    return answer
