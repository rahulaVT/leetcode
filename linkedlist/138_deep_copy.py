"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        ## METHOD 1 : 2N
        # dic = {}
        # m = n = head
        # while m:
        #     # keys are the original nodes and values are the copy nodes
        #     dic[m] = Node(m.val)
        #     m = m.next
        # # print(dic)
        # while n:
        #     # assign value's(copy node) next to current(original node) next value. 
        #     # using get() because it will give None if not found.
        #     dic[n].next = dic.get(n.next)
        #     dic[n].random = dic.get(n.random)
        #     n = n.next
        # return dic.get(head)
        
        ## METHOD 2: N
        dic = collections.defaultdict(lambda: Node(0))
        n = head
        dic[None] = None
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
