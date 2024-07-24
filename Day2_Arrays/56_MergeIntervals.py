'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

# Approach:
# The function first sorts the intervals based on their starting values. Then, it iterates through the sorted intervals, 
# merging overlapping intervals by extending the end of the current interval as needed and appending the merged intervals to the result list.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        res=[]
        i,n=0,len(intervals)
        while i<n-1:
            num1=intervals[i][0]
            num2=intervals[i][1]
            while i<n-1 and intervals[i+1][0]<=num2:
                num2=max(intervals[i+1][1],num2)
                i+=1
            res.append([num1,num2])
            i+=1
        if res[len(res)-1][1]!=intervals[n-1][1] and intervals[n-1][1]>num2:
            res.append(intervals[n-1])
        return res
