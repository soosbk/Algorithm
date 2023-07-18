n,k=map(int, input().split())
coin_list=[]
for i in range(n):
	coin=int(input())
	coin_list.append(coin)

answer=0
idx=len(coin_list)-1 #오름차순으로 입력되었기 때문에
while (k>0) and (idx>=0):
	if coin_list[idx]>k: 
		idx-=1
		continue
	answer+=(k//coin_list[idx])
	k%=coin_list[idx]

print(answer)
