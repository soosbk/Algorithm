from bisect import bisect_left, bisect_right


def count_by_bisect(array,value):
	left_idx=bisect_left(array,value)
	right_idx=bisect_right(array,value)

	return right_idx-left_idx




n,x=map(int,input().split())

array=list(map(int,input().split()))



print(count_by_bisect(array,x))



def first(array,target,start,end):
	if start> end: return None
	mid=(start+end)//2
	if (mid==0 or target>array[mid-1]) and array[mid]==target:
		return mid #찾던 값이 가장 끝에 있거나, 전꺼랑 다를게 없는 경우
	elif target<=array[mid]:
		return first(array,target,start, mid-1)
	else:
		return first(array,target,mid+1,end)

def last(array,target,start,end):
	if start>end: return None
	mid=(start+end)//2
	if (mid==n-1 or target<array[mid+1]) and array[mid]==target:
		return mid
	elif target>=array[mid]:
		return last(array,target,mid+1,end)
	else:
		return last(array,target,start,mid-1)

print(last(array,x,0,n-1)-first(array,x,0,n-1)+1)
