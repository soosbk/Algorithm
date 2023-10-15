#95% <- 미완성


from heapq import heappush, heappop
def solution(jobs):
    q=[]
    if len(jobs)==1: return jobs[0][1]
    cnt=len(jobs)
    jobs.sort()
    end=jobs[0][0]+jobs[0][1] #start+time
    answer=jobs[0][1] #time <-0이 걸린 시간
    for job in jobs[1:]:
        start,time=job #now
        if end>start:
            heappush(q,[time,start])
        elif end==start:
            heappush(q,[time,start])
            t,s=heappop(q)
            end+=t
            answer+=(end-s)
        else: #end<start
            if q:
                t,s=heappop(q)
                end+=t
                answer+=(end-s)
                heappush(q,[time,start])
            else:
                end=time+start
                answer+=time
            
    if q:     
        new_q=[]
        while q:
            print(q)
            n=sorted(q,key=lambda x: (x[1],x[0]))     
            if n[0][1]>end:
                print(".")
                t,s=n[0]
                end=s+t
                answer+=t
                q=n[1:]
            if len(q)<=0: break
            t,s=heappop(q)
            if s>end:
                heappush(new_q,[t,s])
                continue
            else:
                end+=t
                answer+=(end-s)
            if new_q:
                for i in new_q:
                    heappush(q,i)
                new_q=[]
    return answer//cnt

#print(solution([[0, 6], [2, 8], [3, 7], [7, 1], [11, 11], [19, 25], [30, 15], [32, 6], [40, 3]] )) #9
