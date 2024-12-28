class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            sumNums = num + carry
            if sumNums == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = sumNums
        
        if carry == 1:
            digits = [1] + digits

        return digits
