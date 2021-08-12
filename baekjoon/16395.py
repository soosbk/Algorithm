li=input().split(" ")
row=int(li[0])-1
col=int(li[1])-1
output=1
if col>(row-col):
	for i in range(row,col,-1):
		output*=i
	for i in range(1,(row-col)+1):
		output/=i
else:
	for i in range(row, row-col,-1):
		output*=i
	for i in range(1,col+1):
		output/=i
print(int(output))
