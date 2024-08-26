'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

# This approach finds the maximum number of consecutive 1s in a binary array. 
# It iterates through the list, incrementing a counter `count` for each `1` found. 
# When a `0` is encountered, the current streak's length is compared to the maximum found so far (`maxi`).
# After the loop, it returns the maximum between the final streak and `maxi` to account for sequences ending at the last element.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for num in nums:
            if num==1:
                count+=1
            else:
                maxi=max(count,maxi)
                count=0
        return max(count,maxi)
