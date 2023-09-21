def solution(id_list, report, k):
    answer = [0]*len(id_list)
    user={id_list[i]: i for i in range(len(id_list))}
    s={key:[] for key in id_list}
    report=list(set(report))
    for id in report:
        a=id.split(" ")
        s[a[1]].append(a[0])
        
    for key in s:
        if len(s[key])>=k:
            for u in s[key]:
                answer[user[u]]+=1
            
        
        
    return answer
