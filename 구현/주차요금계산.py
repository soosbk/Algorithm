def time_calculator(fees,times):
	new_fees=[]
	f=0
	for i in range(0,len(times),2): #01234
		f+=(int(times[i+1][:2])-int(times[i][:2]))*60+int(times[i+1][3:])-int(times[i][3:])
	money=fees[1]
	if f>fees[0]:
		f-=fees[0]
		money+=(f//fees[2])*fees[3]
		if f%fees[2]:
			money+=fees[3]

	return money



	

def solution(fees, records):
    answer = []
    cars={}
    answers=[]
    for record in records:
    	lst=record.split(" ")
    	if lst[2]=='IN':
    		if lst[1] in cars:
    			cars[lst[1]].append(lst[0])
    		else:
    			cars[lst[1]]=[lst[0]]
    	else:
    		cars[lst[1]].append(lst[0])


    for key in cars:
    	if len(cars[key])%2==1: 
    		cars[key].append("23:59")
    	answers.append([key,time_calculator(fees,cars[key])])


    answers.sort()
    answer=[i for x,i in answers]

    return answer


