# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        answer = []
        stack = []
        index = 0
        while head:
            answer.append(0)
            curr_val = head.val
            while stack and stack[-1][0] < curr_val:
                answer[stack.pop()[1]] = curr_val
            stack.append((curr_val,index))
            index+=1
            head = head.next
        # print(stack)
        return answer
