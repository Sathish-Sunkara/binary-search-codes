# this is sorted fully ie :the matrix is need to follow the condition that mat[i][last] <  mat[i+1][first]
# if u flatten the 2d array then result will become the sorted 1d array

def indices(n,m,mid):
    # return i,j values
    return mid // m , mid % m

def values(n,m,r,c):
    # returs mid value
    return r*m + c
def binary_search(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    start = 0
    end = m*n - 1
    
    while start <= end :
        mid = (start+end) // 2
        r,c = indices(n,m,mid)
        if matrix[r][c] == target :
            return (r,c)
        elif matrix[r][c] > target :
            mid = values(n,m,r,c)
            end = mid - 1
        else:
            mid = values(n,m,r,c)
            start = mid + 1
    return (-1,-1)



matrix = [
    [11,23,45,67] , 
    [78,89,98,100] , 
    [121, 132, 234, 345] , 
    [456,678,789,999]
]
target = 678      # 3,1
print(binary_search(matrix,target))

        

