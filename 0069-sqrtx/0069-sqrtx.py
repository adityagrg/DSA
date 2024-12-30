class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        prev = 1
        for i in range(2, x):
            if i * i > x:
                break
            else:
                prev = i
        
        return prev