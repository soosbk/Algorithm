n=int(input())

array=list(map(int,input().split()))






def search(array,start,end):
	if start>end: return -1
	mid=(start+end)//2
	if array[mid]>mid: 
		return search(array,start,mid-1)
	elif array[mid]==mid: 
		return mid
	else: 
		return search(array,mid+1,end)







mid=search(array,0,n-1)
print(mid)
