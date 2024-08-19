'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# The approach merges two sorted linked lists into one by iteratively comparing the current nodes of `list1` and `list2`, appending the smaller node to the merged list (`temp`). 
# After one of the lists is exhausted, the remaining nodes of the other list are appended directly. 
# The merged list is returned starting from the node following the `dummy` node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # v=[]
        # while list1:
        #     v.append(list1.val)
        #     list1=list1.next
        # while list2:
        #     v.append(list2.val)
        #     list2=list2.next
        # v.sort()
        # temp=ListNode()
        # head=temp
        # for i in v:
        #     temp.next=ListNode(i)
        #     temp=temp.next
        # head=head.next
        # return head

        dummy=temp=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                temp.next=list1
                temp=list1
                list1=list1.next                
            else:
                temp.next=list2
                temp=list2
                list2=list2.next
        if list1 or list2:
            temp.next=list1 if list1 else list2
        return dummy.next
        
