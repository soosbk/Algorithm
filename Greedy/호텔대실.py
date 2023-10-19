def solution(book_time):
    room_end=["00:00"] * (len(book_time)+1)
    book_time.sort()
    for time in book_time:
        start,end=time
        for num in range(0,len(book_time)+1):
            if room_end[num]<=start:
                h=int(end[:2])
                m=int(end[3:])+10
                if m>60:
                    m%=60
                    h+=1
                sh=str(h)
                sm=str(m)
                if len(sh)==1: sh='0'+sh
                if len(sm)==1: sm='0'+sm
                room_end[num]=str(h)+":"+str(m)
                
                break
    return len(room_end)-room_end.count("00:00")
