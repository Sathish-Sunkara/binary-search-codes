"""
the binary search using recursion
"""

def binary(arr,target,start,end) :
    if start > end :
        return -1
    mid = (start+end) // 2
    if arr[mid] == target :
        return mid
    # splitting the array
    if arr[mid] > target :
        return binary(arr,target,start,mid-1)
    return binary(arr,target,mid+1,end)


arr = [2,4,6,8,9,13]
target = 9
ans = binary(arr,target,0,len(arr)-1)
print(ans) 
