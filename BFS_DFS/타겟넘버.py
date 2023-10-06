

def solution(numbers, target):
    answer = 0
    stack=[[-numbers[0],0],[numbers[0],0]]
    while stack:
        num,time=stack.pop()
        time+=1
        if time>=len(numbers):
            if target==num: 
                    answer+=1
            continue
        stack.append([num+numbers[time],time])
        stack.append([num-numbers[time],time])
    
    return answer
