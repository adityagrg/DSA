class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        newX = 0
        while temp != 0:
            rem = temp % 10
            newX = newX * 10 + rem
            temp = temp // 10
        
        if newX == x:
            return True
        else:
            return False