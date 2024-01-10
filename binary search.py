def binary_asc(nums,key):
     start = 0
     end = len(nums) - 1
     while start <= end :
          
          mid = (start + end) // 2
          if nums[mid] == key :
               return mid
          elif key < nums[mid]:
               end = mid - 1
          else :
               start = mid + 1

     return -1

def binary_desc(nums,key):
     start = 0
     end = len(nums) - 1
     while start <= end :
          
          mid = (start + end) // 2
          if nums[mid] == key :
               return mid
          elif key > nums[mid]:
               end = mid - 1
          else :
               start = mid + 1

     return -1




def binarysearch(nums,key):
     if nums[0] < nums[len(nums)//2] :
          return binary_asc(nums,key)
     else:
          return binary_desc(nums,key)
     
     

nums = [9,9,8,6,4,3,2,1]
nums = nums[::-1]
key = 3
print(binarysearch(nums,key))
        
          
          