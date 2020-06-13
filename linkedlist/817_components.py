# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        result = 0
        while head:
            if head.val in G and (head.next == None or head.next.val not in G):
                # print(head.val)
                result+=1
            head = head.next
        return result
