def solution(phone_book):
    new_phone_book={}
    for p in phone_book:
        if int(p[0]) not in new_phone_book: new_phone_book[int(p[0])]=[p]
        else: new_phone_book[int(p[0])].append(p)
    
    for k in new_phone_book:
        lst=sorted(new_phone_book[k])
        nowstr=lst[0]
        for i in range(1,len(lst)):
            if lst[i].startswith(nowstr):
                    return False
            nowstr=lst[i]
    return True
    
