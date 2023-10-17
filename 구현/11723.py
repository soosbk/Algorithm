import sys
n=int(input())
s=[0]*21
input=sys.stdin.readline
for _ in range(n):
    l=input()
    if " " in l:
        lst=l[:-1].split(" ")
        lst[1]=int(lst[1])
        
    else:
        lst=[l[:-1]]
    if lst[0]=="add":
        s[lst[1]]=1

    elif lst[0]=="remove":
        s[lst[1]]=0


    elif lst[0]=="check":
        if s[lst[1]]:
            print(1)
        else:
            print(0)

    elif lst[0]=="toggle":
        if s[lst[1]]==1:
            s[lst[1]]=0
        elif s[lst[1]]==0:
            s[lst[1]]=1

    elif lst[0]=="all":
        s=[1]*21
        

    elif lst[0]=="empty":
        s=[0]*21
