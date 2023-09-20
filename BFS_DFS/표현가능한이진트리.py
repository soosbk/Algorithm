import math


def dfs(b, parent):
    # 현재 노드 값
    current = len(b) // 2
    if current<0 or current>=len(b) or len(b)<1: return True
    current_result = b[current]
    
    # 부모 노드가 '0'이고 자식 노드 중에 '1'이 있는 경우 '0' 반환, 그렇지 않으면 '1' 반환
    if parent == '0' and current_result=='1' :
        return False
    else:
        return dfs(b[:current],current_result) and dfs(b[current+1:],current_result)

def solution(numbers):
    answer = []
    for number in numbers:
        b = bin(number)[2:]
        cnt = math.ceil(math.log2(len(b) + 1))
        n = 2**cnt - 1
        if len(b)!=n: 
            b='0'*(n-len(b))+b

        if dfs(b, 1):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer
