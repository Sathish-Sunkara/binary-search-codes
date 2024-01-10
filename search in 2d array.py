# the 2d array is sorted in row wise and column wise also
def create_array(n,m) :
    matrix = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(input())
    return matrix

def binary_search(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = len(matrix[0]) - 1

    while row < n or col >= 0 :
        if matrix[row][col] == target :
            return (row,col)
        elif target > matrix[row][col] :
            row += 1
        else:
            col -= 1
    return (-1,-1)

n = int(input("enter the rows")) 
m = int(input("enter the columns"))
target = int(input("enter the target"))
matrix = create_array(n,m)
print(matrix)
print(binary_search(matrix,target)) 
# the matrix no need to follow the condition that mat[i][last] <  mat[i+1][first]