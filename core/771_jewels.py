class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # if not J or not S: return 0
        # s = set(J)
        # res = 0
        # for i in S:
        #     if i in s:
        #         res+=1
        # return res
        
        return sum(map(S.count,J))
                
