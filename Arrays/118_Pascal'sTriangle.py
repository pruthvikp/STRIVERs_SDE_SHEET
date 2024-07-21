'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
'''

# Approach 1: Iterative Construction
# Initialize the First Row: Start with a list containing a single row with the number [1].
# Prepare Empty Rows: Create empty lists for the remaining rows.
# Construct Each Row:
# -The first element of each row is always 1.
# -For each position in the current row (except the first and last), sum the two elements directly above from the previous row.
# -The last element of each row is always 1.

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        new=[[1]]
        for _ in range(numRows-1):
            new.append([])
        for i in range(1,numRows):
            new[i].append(1)
            for j in range(len(new[i-1])-1):
                new[i].append(new[i-1][j]+new[i-1][j+1])
            new[i].append(1)
        return new

# Approach 2: Combinatorial Calculation
# Define a helper function nCr(n, r) to compute the binomial coefficient.
# For each row n, compute each element using the formula (n-1)C(r-1)
# Append the computed elements to the current row.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def nCr(n,r):
            res=1
            for i in range(r):
                res*=(n-i)
                res//=(i+1)
            return res
        
        new=[]
        for n in range(1,numRows+1):
            now=[]
            for r in range(1,n+1):
                now.append(nCr(n-1,r-1))
            new.append(now)
        
        return new
