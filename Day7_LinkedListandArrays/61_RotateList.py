'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

# Approach:
# The solution first calculates the length `n` of the linked list and adjusts `k` to be within the list's length. 
# If `k` is zero after adjustment, the list remains unchanged. 
# Otherwise, the list is split into two parts: the first part ends just before the new head, and the second part starts at the new head. 
# The two parts are then reconnected to achieve the rotation, and the new head is returned.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ptr=head
        n=1
        while ptr.next:
            n+=1
            ptr=ptr.next
        k=k%n
        if k==0:
            return head
        temp=head
        for _ in range(n-k-1):
            temp=temp.next
        new=temp.next
        temp.next=None
        ptr.next=head
        head=new

        return head
