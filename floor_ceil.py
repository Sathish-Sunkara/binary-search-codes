#this gives the floor number or ceil number to the given target in sorted array
#same as binary search when target found return it then instead of -1 we return end or start because floor or ceil number present
# at those places (because when boundaries comes closer in proccess they search for target if target not found then thet at same value)
#(i.e start = end then again end move to the place where the floor value of the target is prezent same happened in ceil also)

class Search:
    def __init__(self,nums,key):
        self.array = nums
        self.target = key
        self.start = 0
        self.end = len(self.array) - 1

    # return the the target or just less than the target(floor)
    def floor(self):
        start = 0
        end = self.end

        while start <= end :
          
            mid = (start + end) // 2

            if self.array[mid] == self.target :
                return mid
            elif self.target < self.array[mid]:
                end = mid - 1
            else :
               start = mid + 1
            print(start , end)
        print(start , end)

        return end
    # it gives target or just grater than target value
    def ceil(self):
        start = 0
        end = self.end

        while start <= end :
          
            mid = (start + end) // 2

            if self.array[mid] == self.target :
                return mid
            elif self.target < self.array[mid]:
                end = mid - 1
            else :
               start = mid + 1

        return start
    

nums = [1,1,1,1,2,3,3,5,5,7,8,9] 
target = 4
b = Search(nums,target)
print(b.floor())






