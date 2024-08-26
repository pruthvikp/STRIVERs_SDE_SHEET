'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

# Approach 1: BruteForce (TLE)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        x=[nums[i],nums[j],nums[k]]
                        x.sort()
                        if x not in res:
                            res.append(x)
        return list(res)


# Approach 2: Hashing (TLE)
# The `threeSum` function finds all unique triplets in the list `nums` that sum to zero by using a set to track pairs and check if the third required value exists. 
# For each element, it iterates through the remaining elements, calculates the required third number, and checks if it exists in the set. 
# The result is stored as sorted tuples in a set to ensure uniqueness.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d={}
        res=set()
        n=len(nums)
        for i in range(n):
            d=set()
            for j in range(i+1,n):
                y=-(nums[i]+nums[j])
                if y in d:
                    x=[nums[i],nums[j],y]
                    x.sort()
                    res.add(tuple(x))
                d.add(nums[j])

        return list(res)


# Approach 3: Optimal
# This function finds all unique triplets that sum to zero by first sorting the list. 
# It then iterates through each number, using two pointers (`j` and `k`) to find pairs that, when combined with the current number, sum to zero. 
# The algorithm skips duplicates to ensure unique triplets and adjusts the pointers based on the current sum, returning the result as a list of triplets.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res
