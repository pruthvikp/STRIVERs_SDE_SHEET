'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
 
Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

# Approach 1: 
# Sort the array. After that, if there is any duplicate number they will be adjacent.
# So we simply have to check if nums[i]==nums[i+1] and if it is true,nums[i] is the duplicate number.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]

# Approach 2:
# Approach: Take a frequency array of size N+1 and initialize it to 0. 
# Now traverse through the array and if the frequency of the element is 0 increase it by 1, else if the frequency is not 0 then that element is the required answer.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=[0]*(len(nums))
        for num in nums:
            if freq[num]==0:
                freq[num]+=1
            else:
                return num

# Approach 3: Floyd's Tortoise and Hare (Cycle Detection) algorithm
# First detect a cycle through slow and fast pointers, then find the cycle's entry point which corresponds to the duplicate. 
# Once a cycle is detected, reset one pointer to the start and move both pointers one step at a time identifies the duplicate number when they meet again.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        fast=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
               
