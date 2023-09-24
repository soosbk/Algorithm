def solution(number, k):
    answer = ''
    stack=[]
    for i in number:
        if len(stack)==0:
            stack.append(i)
            continue
        while stack and stack[-1]<i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
        if len(stack)==len(number)-k:
            break
    return "".join(stack)
