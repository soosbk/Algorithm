def solution(today, terms, privacies):
    answer = []
    term={}
    for t in terms:
        term[t[0]]=int(t[2:])
    ay=int(today[:4])
    am=int(today[5:7])
    ad=int(today[8:])
    
    end_date=[]
    for i in range(len(privacies)):
        date=privacies[i][:-2]
        year=int(date[:4])
        month=int(date[5:7])+term[privacies[i][-1]]
        day=int(date[8:])-1
        
        if day<1:
            month-=1
            day=28
        if month>12:
            year+=month//12
            month%=12
        if month<1:
            year-=1
            month+=12
        
        #비교
        if ay>year or (year==ay and am>month) or (year==ay and am==month and ad>day): answer.append(i+1)
        
        
        
    return answer
