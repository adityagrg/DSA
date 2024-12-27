class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        mapping = {}
        mapping[1] = 1
        mapping[2] = 2

        for i in range(3, n + 1):
            mapping[i] = mapping[i-2] + mapping[i-1]
        
        return mapping[n]