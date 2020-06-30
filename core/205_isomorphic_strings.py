class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        dic = {} #store mapping 
        mapped = set() # store already mapped characters
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in dic:
                if dic[x] != y:
                    return False
                
            else:
                if y in mapped: return False
                dic[x] = y
                mapped.add(y)
        return True
