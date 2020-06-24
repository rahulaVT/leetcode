# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy= ListNode(0)
        prev.next = head
        # dummy.next = head
        # print(prev.next.val,dummy.next.val)
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next
    
            
