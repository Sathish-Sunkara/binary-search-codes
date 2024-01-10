# search element in infinity sorted array 
# represent array as two boundaries (ofcourse here indices are numbers)
def binary_search(nums,left , right , key):

     while left <= right :
          
          mid = (left + right) // 2
          if nums[mid] == key :
               return mid
          elif key < nums[mid]:
               right = mid - 1
          else :
               left = mid + 1

def infinite_search(nums,key):
    start = 0
    end = 1
    while key > nums[end] :
          start = end + 1
          end = 2*end # here array is infinite no problem otherwise it more than ending boundary for that we use "if end > len(arr) then end = len(arr)-1"

    ans = binary_search(nums,start,end,key)
    return ans
    


array = [1,3,6,8,9,12,14,34,56,67,89,123,234,346,789] # consider it as a infinite array
target = 346
ans = infinite_search(array , target) # to find target element index as ans
print(ans)
    
