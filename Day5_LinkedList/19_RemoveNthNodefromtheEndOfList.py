'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
'''


# The approach uses two pointers, `slow` and `fast`, to locate the nth node from the end of the list. 
# The `fast` pointer is moved `n-1` steps ahead, then both pointers move together until `fast` reaches the end, positioning `slow` at the target node. 
# The target node is then removed by adjusting the pointers, and the modified list is returned.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow=fast=head
        for _ in range(n-1):
            if fast is None:
                return None
            fast=fast.next
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next
        if slow==head:
            head=slow.next
            slow.next=None
        elif slow.next is None:
            pre.next=None
        else:
            pre.next=slow.next
            slow.next=None
        return head
    
