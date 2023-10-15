import sys

input=sys.stdin.readline



while True:
	sen=input()
	if len(sen)==2 and sen[0]=='.': break
	stack=[]
	n=True
	for i in range(len(sen)-2):
		if sen[i]=='(' or sen[i]=='[':
			stack.append(sen[i])
		elif sen[i]==')':
			if len(stack)>0 and stack[-1]=='(': stack.pop()
			else:
				n=False
				break
		elif sen[i]==']':
			if len(stack)>0 and stack[-1]=='[': stack.pop()
			else:
				n=False
				break

	if len(stack)>0 or n==False:
		print("no")
	else: print("yes")
