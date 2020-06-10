# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## METHOD 1 : not optimal. was following the strategy used in sorted array
        # unique = head
        # result = unique
        # while head.next:
        #     if head.val != head.next.val:
        #         unique.next = head.next
        #         unique = unique.next
        #     head = head.next
        # return result
        
        # METHOD 2: Using solution
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # print("inside")
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
            
