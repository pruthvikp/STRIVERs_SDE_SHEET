'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# Bruteforce- TLE
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:   
        res=float('-inf')
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                res=max(sum,res)
        return res

# Kadane's algorithm
# The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0. 
# A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.

# Here, we will iterate the given array with a single loop and while iterating we will add the elements in a sum variable. 
# Now, if at any point the sum becomes less than 0, we will set the sum as 0 as we are not going to consider any subarray with a negative sum.
# Among all the sums calculated, we will consider the maximum one.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=float('-inf')
        sum=0
        for num in nums:
            sum+=num
            res=max(sum,res)
            if sum<0:
                sum=0
      
        return res
