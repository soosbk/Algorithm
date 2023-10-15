name_dic={
"A":3, "B":2, "C":1,"D":2,	"E":4,	"F":3,	"G":1,	"H":3,	"I":1,	"J":1,	"K":3,	
"L":1,	"M":3,	"N":2,	"O":1,"P":2,	"Q":2,	'R':2,	"S":1,	"T"	:2,"U":1,	
"V":1,	"W":1,	"X":2,	"Y":2,	"Z":1
}

def find_percent(stack):
	if len(stack)==2: 
		return stack
	s=[]
	for i in range(len(stack)-1):
		s.append((stack[i]+stack[i+1])%10)

	return s


a,b=map(int,input().split())
stra,strb=map(str,input().split())

stack=[]


for i in range(min(a,b)):
	stack.append(name_dic[stra[i]])
	stack.append(name_dic[strb[i]])

if a<b:
	for j in range(a,b):
		stack.append(name_dic[strb[j]])
elif a>b:
	for j in range(b,a):
		stack.append(name_dic[stra[j]])
while len(stack)>2:
	stack=find_percent(stack)

print(str(stack[0]*10+stack[1])+"%")

