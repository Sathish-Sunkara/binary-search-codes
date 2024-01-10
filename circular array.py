#it finds the largest element in the in  the circular array

def search(nums):
    start = 0
    end = len(nums) - 1
    while start <= end :
        mid = (start+end) // 2
        # target condition 
        if nums[mid] > nums[mid+1] :
            return nums[mid]
        if nums[mid-1] > nums[mid] :
            return nums[mid-1]
        elif nums[start] < nums[mid] :
            start = mid + 1
        else:
            end = mid - 2
    return -1

nums = [6,6,7,7,7,8,8,8,8,8,9,9,123,123,124,124,0,0,0,0,1,2,2,2,3,4,4,5,5]
print(search(nums))
