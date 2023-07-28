n=int(input())
infos=[]

for i in range(n):
	infos.append(input().split())


# 국어 내림 -> 영어 증가 -> 수학 감소 -> 이름 증가

answers=sorted(infos,key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for answer in answers:
	print(answer[0])
