# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = 0
        curr = root
        while curr:
            l+=1
            curr = curr.next
        # print(l)
        width = l//k # length of most parts
        rem = l%k # extra length of first rem parts
        ans = []
        
        for i in range(k):
            temp = write = ListNode(None)
            for j in range(width+(i<rem)):
                write.next = write = ListNode(root.val)
                if root: root = root.next
            ans.append(temp.next)
        return ans
                
            
