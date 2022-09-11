def reverseArray(a):
	rev_Array = []
	i = len(a)-1

	while i >= 0:
		
		rev_Array.append(a[i])
		i-=1
	return rev_Array



arr = [1,2,3,4,5]	
print(reverseArray(arr))
