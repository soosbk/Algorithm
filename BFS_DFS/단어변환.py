from collections import deque
def solution(begin, target, words):
    if target not in words: return 0
    q=deque([[begin,0]])
    lst=[]
    for i in range(len(begin)):
        t=[]
        for word in words:
            t.append(word[:i]+word[i+1:])
        lst.append(t)
    while q:
        now,t=q.popleft()
        if now==target:
            return t
        if t>len(words)*len(words[0]): return 0
        for i in range(len(now)):
            new_word=now[:i]+now[i+1:]
            for w in range(len(lst[i])):
                if new_word==lst[i][w] and now!=words[w]:
                    q.append([words[w],t+1])
            
    
    return 0
