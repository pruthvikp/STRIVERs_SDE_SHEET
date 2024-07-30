'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
''' 

# Bruteforce approach:
# First, we will use a loop(say i) to select the indices of the array one by one.
# For every index i, we will traverse through the remaining array using another loop(say j) to find the other number such that the sum is equal to the target (i.e. nums[i] + nums[j] = target).
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out=[]
        n=len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]


# Better approach:
# A hash table is used to store the indices of the elements in the list as they are encountered. 
# For each element, it checks if the complement (target minus the current element) exists in the hash table, and if so, returns the indices of the current element and its complement.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i,num in enumerate(nums):
            if target-num in h:
                return [i,h[target-num]]             
            else:
                h[num]=i


# Optimal approach: 2 pointers - Tells only if solution exists or not
# We will sort the given array first.
# Now, we will take two pointers i.e. left, which points to the first index, and right, which points to the last index.
# Now using a loop we will check the sum of nums[left] and nums[right] until left < right.
# -If nums[left] + nums[right] > sum, we will decrement the right pointer.
# -If nums[left] + nums[right] < sum, we will increment the left pointer.
# -If nums[left] + nums[right] == sum, we will return the result.
# Finally, if no results are found we will return “No” or {-1, -1}.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l,r=0,len(nums)-1
        while l<len(nums) and r>=0:
            if nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                return True
        return False
