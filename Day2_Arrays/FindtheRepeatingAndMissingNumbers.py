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

# Approach 2:

# S = the summation of all the elements in the given array.
# Summation of the first N numbers Sn = (N*(N+1))/2
# Therefore, S - Sn = X - Y…………………equation 1

# S2 = the summation of squares of all the elements in the given array.
# Now, we know the summation of squares of the first N numbers S2n = (N*(N+1)*(2N+1))/6
# Therefore, S2-S2n = X2-Y2...................equation 2

# X+Y = (S2 - S2n) / (X-Y)

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        
        S=sum(A)
        Sn=n*(n+1)//2
        val1=Sn-S
        
        S2=0
        Sn2=(n*(n+1)*(2*n+1))//6
        for num in A:
            S2+=num*num
        val2=Sn2-S2

        val2 = val2 // val1
        X=(val2+val1)//2
        Y=X-val1
        return [Y,X]
