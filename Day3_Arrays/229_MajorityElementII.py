'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]
Example 2:
Input: nums = [1]
Output: [1]
Example 3:
Input: nums = [1,2]
Output: [1,2]
 
Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

Follow up: Could you solve the problem in linear time and in O(1) space?
'''

# Approach 1: Using hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
            if d[num]>(n//3) and num not in res:
                res.append(num)
                if len(res)==2:
                    return res
        return res

# Approach 2: Extended Boyer-Moore's voting algorithm
# Initialize 4 variables: cnt1 & cnt2 –  for tracking the counts of elements, el1 & el2 – for storing the majority of elements.
# Traverse through the given array.
# -If cnt1 is 0 and the current element is not el2 then store the current element of the array as el1 along with increasing the cnt1 value by 1.
# -If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 along with increasing the cnt2 value by 1.
# -If the current element and el1 are the same increase the cnt1 by 1.
# -If the current element and el2 are the same increase the cnt2 by 1.
# -Other than all the above cases: decrease cnt1 and cnt2 by 1.
# The integers present in el1 & el2 should be the result we are expecting. So, using another loop, we will manually check their counts if they are greater than the floor(N/3).
  
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
  
        c1,c2=0,0
        ele1,ele2=None,None
        for num in nums:
            if c1==0 and num!=ele2:
                c1=1
                ele1=num
            elif c2==0 and num!=ele1:
                c2=1
                ele2=num
            elif num==ele1:
                c1+=1
            elif num==ele2:
                c2+=1
            else:
                c1-=1
                c2-=1
        
        res=[]
        count1,count2=0,0
        for num in nums:
            if num==ele1:
                count1+=1
            elif num==ele2:
                count2+=1
        if count1>(len(nums)//3):
            res.append(ele1)
        if count2>(len(nums)//3):
            res.append(ele2)
        
        return res
        
