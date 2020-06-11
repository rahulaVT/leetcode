# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
#         curr = head
#         if curr.val == val:
#             return
        
#         while curr and curr.next:
#             if curr.val == val:
#                 curr.val = curr.next.val
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
    
#         return head
        
        curr = ListNode(0)
        curr.next = head
        dummy = curr
        while curr and curr.next:
            if curr.next.val == val:
                print("if")
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
    
            
