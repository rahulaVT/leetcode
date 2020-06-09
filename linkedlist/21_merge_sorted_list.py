# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        final = ListNode(0)
        head = final
        while l1 and l2:
            if l1.val<l2.val:
                final.next = l1
                l1 = l1.next
                final = final.next
            else:
                final.next = l2
                l2 = l2.next
                final = final.next
        final.next = l1 or l2
        return head.next
                
