# Not in leetcode, solved in InterviewBit

'''
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.

Example:
Input:[3 1 2 5 3] 
Output:[3, 4] 
'''

# The approach calculates the sum of the array and uses a frequency array to detect the duplicate number. 
# By subtracting the actual sum from the expected sum and adjusting for the duplicate, it identifies the missing number.
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        summation=sum(A)
        freq=[0]*(n+1)
        res=[]
        for num in A:
            if freq[num]==0:
                freq[num]+=1
            else:
                res.append(num)
                break
        x=(n*(n+1)//2)-((summation)-res[0])
        res.append(x)
        return res
