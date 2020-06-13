# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # odd = head
        # if head.next:
        #     even = head.next
        # else:
        #     return head
        # result = ListNode(0)
        # # result.next = odd
        # temp = result 
        # while odd:
        #     print(odd.val)
        #     result.next = odd
        #     result = result.next
        #     odd = None if odd.next==None else odd.next.next
        # while even:
        #     print(even.val)
        #     result.next = even
        #     result = result.next
        #     even = None if even.next==None else even.next.next
        # return temp.next
        
        if head == None:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
            
