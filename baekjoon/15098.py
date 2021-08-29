inp=input()

li=inp.split(" ")

repeat=False

checked=[]
for i in range(0,len(li)):
	if li[i] in checked:
		repeat=True
		break

	else: checked.append(li[i])



if repeat: print("no")
else: print("yes")
