class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
                if d[num]>len(nums)//2:
                    return num
            else:
                d[num]=1
