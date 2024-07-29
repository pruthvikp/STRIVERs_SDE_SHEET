'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

# Approach:
# Use a hashmap and store as (key, value) pairs. 
# Here the key will be the element of the array and the value will be the number of times it occurs. 
# Traverse the array and update the value of the key. Simultaneously check if the value is greater than the floor of N/2. If yes, return the key. Else iterate forward.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
            if d[num]>len(nums)//2:
                return num


# Optimal approach: Moore's Voting Algorithm
# Initialize 2 variables: Count –  for tracking the count of element, Element – for which element we are counting
# Traverse through the given array.
# -If Count is 0 then store the current element of the array as Element.
# -If the current element and Element are the same increase the Count by 1.
# -If they are different decrease the Count by 1.
# The integer present in Element should be the result we are expecting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,ele=0,None
        for num in nums:
            if count==0:
                count+=1
                ele=num
            elif num==ele:
                count+=1
            else:
                count-=1
        return ele
