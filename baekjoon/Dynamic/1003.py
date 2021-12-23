time=int(input())


for _ in range(time):
  fib_base_lst=[[1,0],[0,1]]
  n=int(input())
  if n>1: 
   for i in range(2,n+1):
    fib_base_lst.append([fib_base_lst[i-1][0]+fib_base_lst[i-2][0],fib_base_lst[i-1][1]+fib_base_lst[i-2][1]])

  print("{} {}".format(fib_base_lst[n][0],fib_base_lst[n][1]))
   
