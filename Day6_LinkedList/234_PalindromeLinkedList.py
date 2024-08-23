'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
'''

# Approach 1:
# Traverse the linked list and store each node's value in a list a.
# Create a copy of a in list b and then reverse a.
# Compare the original list b with the reversed list a; if they are identical, the linked list is a palindrome, so return True, otherwise return False.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        b=a[:]
        a.reverse()
        return True if a==b else False

# Approach 2:
# Traverse the linked list and store each node's value in a list a.
# Reset the pointer to the head of the list and then compare each node's value with the elements popped from the end of a.
# If all values match, return True indicating the list is a palindrome; if any value doesn't match, return False.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        temp=head
        while head:
            a.append(head.val)
            head=head.next
        
        while temp:
            if a.pop()!=temp.val:
                return False
            temp=temp.next
        
        return True

# Approach 3:
# Use two pointers, slow and fast, to find the middle of the linked list, with fast moving twice as fast as slow.
# Reverse the second half of the list starting from the node after slow.
# Compare the first half and the reversed second half node by node; if all values match, return True, otherwise return False.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        ptr=slow.next
        slow.next=None
        
        temp,temp2,temp3=None,ptr,ptr
        while temp2!=None:
            temp3=temp3.next
            temp2.next=temp
            temp=temp2
            temp2=temp3
        head2=temp

        while head and head2:
            if head.val!=head2.val:
                return False
            head,head2=head.next,head2.next
        return True
