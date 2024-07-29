'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

# Approach 1:
# We will use a loop to select a particular row at a time.
# Next, for every row, i, we will check if it contains the target.
# If target <= matrix[i][m-1]: If this condition is met, we can conclude that row i has the possibility of containing the target.
# So, we will apply binary search on row i, and check if the ‘target’ is present. If it is present, we will return true from this step. Otherwise, we will return false.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(a,low,high,target):
            while low<=high:
                mid=(low+high)//2
                if target<a[mid]:
                    high=mid-1
                elif target>a[mid]:
                    low=mid+1
                else:
                    return True
            return False

        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            if matrix[i][0]<=target<=matrix[i][n-1]:
                return binary_search(matrix[i],0,n-1,target)

# Optimal approach: Apply binary search on the whole matrix
# Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to (NxM)-1.
# Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)
# Eliminate the halves based on the element at index mid: To get the element, we will convert index ‘mid’ to the corresponding cell using the above formula. Here no. of columns of the matrix = M.
# row = mid / M, col = mid % M.
# - If matrix[row][col] == target: We should return true here, as we have found the ‘target’.
# - If matrix[row][col] < target: In this case, we need bigger elements. So, we will eliminate the left half and consider the right half (low = mid+1).
# - If matrix[row][col] > target: In this case, we need smaller elements. So, we will eliminate the right half and consider the left half (high = mid-1).
# Steps 2-3 will be inside a while loop and the loop will end once low crosses high(i.e. low > high). 
# If we are out of the loop, we can say the target does not exist in the matrix. So, we will return false.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        low,high=0,m*n-1
        while low<=high:
            mid=(low+high)//2
            row=mid//n
            col=mid%n
            if target<matrix[row][col]:
                high=mid-1
            elif target>matrix[row][col]:
                low=mid+1
            else:
                return True
        return False
