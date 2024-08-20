'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Approach 1:
# The approach converts the values of two linked lists (`l1` and `l2`) into reversed strings, then into integers, and sums them. 
# The resulting sum is then converted back into a linked list, where each digit is stored in a node, starting from the least significant digit. 
# Finally, the head of this new linked list is returned.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1=""
        ptr1=l1
        while ptr1:
            str1=str(ptr1.val)+str1
            ptr1=ptr1.next
        str2=""
        ptr2=l2
        while ptr2:
            str2=str(ptr2.val)+str2
            ptr2=ptr2.next
        
        str1=int(str1) if str1!="" else 0
        str2=int(str2) if str2!="" else 0

        sum=str1+str2
        ret_head=ListNode(sum%10)
        temp=ret_head
        sum=sum//10
        while sum!=0:
            temp.next=ListNode(sum%10)
            sum=sum//10
            temp=temp.next
        return ret_head


# Approach 2:
