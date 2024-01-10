def search(nums):
    n = len(nums)
    start = 0
    end = n-1
    while start < end :
        mid = (start+end)//2
        if nums[mid] < nums[mid+1] :
            start = mid + 1
        else:
            end = mid
    return nums[start]

nums = [1,8,9,10,10,10,10,10,11,11,11,11,12,12,12,13,13,19,19,19,19,19,18,18,18,17,17,14,14,3,3,1,1]
print(search(nums))



# a possible another method but it not handles the duplicate values efficiently

"""
while start <= end :
        mid = (start+end)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1] :
            return nums[mid]
        elif nums[mid] < nums[mid-1] :
            end = mid - 1
        else:
            start = mid + 1
    return -1
"""