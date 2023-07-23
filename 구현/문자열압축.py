def solution(s):
    answer=len(s)
    for i in range(1,len(s)):
        time=0
        now_str=""
        previous=s[0:i]
        for j in range(0,len(s),i):
            now=s[j:j+i]
            if previous!=now:
                if time==1:
                    now_str+=previous
                else:
                    now_str+=str(time)+previous
                time=1
                previous=now
            else:
                time+=1
        if time==1:
            now_str+=previous
        else:
            now_str+=str(time)+previous
        
        if answer>len(now_str): answer=len(now_str)
                
    return answer
