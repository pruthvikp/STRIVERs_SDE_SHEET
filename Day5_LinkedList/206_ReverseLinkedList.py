'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# The approach iteratively reverses the linked list by traversing it and adjusting the `next` pointers of each node to point to the previous node. 
# A `dummy` node tracks the reversed list's head, and `temp` temporarily stores the next node in the original list. 
# Finally, the `head` is updated to point to the new head of the reversed list, and the reversed list is returned.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head
        dummy=None
        temp=head
        while head!=None:
            temp=temp.next
            head.next=dummy
            dummy=head
            head=temp
        head=dummy
        return head
