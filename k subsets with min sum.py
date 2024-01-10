def sub(nums,k):
    #this return min sum of all possible splits
    start = max(nums)
    end = 0
    for num in nums:
        end += num    
    

    while start < end :
        mid = (start+end)//2
        
        splits = 1
        sum1 = 0
        for num in nums:
            if sum1+num > mid :
                splits =+ 1
                sum1 = num
            else:
                sum1 += num
        if splits > k :
            start = mid + 1
        else :
            end = mid 
    return end

nums = [7,2,5,10,8]
k = 2
print(sub(nums,k))
