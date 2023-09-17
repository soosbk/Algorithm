from itertools import product

def ca(users,user_info):
    membership=0
    fee=0
    for i in range(len(users)):
        if user_info[i]>=users[i][1]:
            membership+=1
        else:
            fee+=user_info[i]
    return membership,fee

        
        
def solution(users, emoticons):
    discount=[40,30,20,10] #0.6,0.7,0.8,0.9
    plus=0
    fee=0
    fees=[]
    for emoticon in emoticons:
        fees.append([int(emoticon*(100-discount[i])/100) for i in range(4)])
    
    for ds in product([0,1,2,3],repeat=len(emoticons)):
        user_info=[0]*len(users) #구매가격
        for i in range(len(ds)):
            for j in range(len(users)):
                u_ds=users[j][0]
                if discount[ds[i]]>=u_ds:
                    user_info[j]+=fees[i][ds[i]]
            
    
                
        m,f=ca(users,user_info)
        
        if plus<m:
            plus=m
            fee=f
        elif plus==m:
            fee=max(fee,f)
            
            
    return [plus,fee]
