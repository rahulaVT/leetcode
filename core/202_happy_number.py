class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n!=1:
            # print("in")
            current_sum = 0
            while n!=0:
                rem = n%10
                n//=10
                current_sum+=(rem**2)
                # print(current_sum)
            if current_sum in sums:
                return False
            else:
                sums.add(current_sum)
                n = current_sum
        return True
            
