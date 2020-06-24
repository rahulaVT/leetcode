# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        
        ## METHOD 1: using set
        # nodes = set()
        # curr = head
        # while curr:
        #     if curr in nodes:
        #         return curr
        #     else:
        #         nodes.add(curr)
        #     curr = curr.next
        # return None
        
        ## METHOD 2: Floyd
        slow = head
        fast = head
        cycle = False
        # Find if there is a cycle and pointer where it's found
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        if not cycle: return
        # from head move one step towards begining of cycle 
        temp = head
        while temp!=slow:
            temp = temp.next
            slow = slow.next
        return slow
