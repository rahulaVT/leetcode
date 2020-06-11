# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the 2nd half
        prev = None
        while slow:
            tempnext = slow.next
            slow.next = prev
            prev = slow
            slow = tempnext
        
        #compare first and 2nd half
        # curr = head
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
    
            
            
