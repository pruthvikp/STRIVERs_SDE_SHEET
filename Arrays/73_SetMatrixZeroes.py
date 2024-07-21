'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

# Approach 1:
# First, we will use two loops(nested loops) to traverse all the cells of the matrix.
# If any cell (i,j) contains the value 0, we will mark all cells in row i and column j with infinity except those which contain 0.
# We will perform step 2 for every cell containing 0.
# Finally, we will mark all the cells containing infinity with 0.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for k in range(n):
                        if matrix[i][k]!=0:
                            matrix[i][k]=float('inf')
                    for k in range(m):
                        if matrix[k][j]!=0:
                            matrix[k][j]=float('inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0

# Approach 2:
# First, we will declare two arrays: a row array of size N and a col array of size M and both are initialized with 0.
# Then, we will use two loops(nested loops) to traverse all the cells of the matrix.
# If any cell (i,j) contains the value 0, we will mark ith index of row array i.e. row[i] and jth index of col array col[j] as 1. It signifies that all the elements in the ith row and jth column will be 0 in the final matrix.
# We will perform step 3 for every cell containing 0.
# Finally, we will again traverse the entire matrix and we will put 0 into all the cells (i, j) for which either row[i] or col[j] is marked as 1.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[0]*m
        col=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(m):
            for j in range(n):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0
