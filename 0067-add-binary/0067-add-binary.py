class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n = len(b)
        remainingZeroes = 0
        s = ""

        if len(a) > len(b):
            n = len(a)
            remainingZeroes = n - len(b)
            for i in range(0, remainingZeroes):
                b = "0" + b
        else:
            n = len(b)
            remainingZeroes = n - len(a)
            for i in range(0, remainingZeroes):
                a = "0" + a

        for i in range(n - 1, -1, -1):
            current = int(a[i]) + int(b[i]) + carry

            if current == 3:
                s = "1" + s
                carry = 1
            elif current == 2:
                s = "0" + s
                carry = 1
            elif current == 1:
                s = "1" + s
                carry = 0
            else:
                s = "0" + s
                carry = 0

        if carry == 1:
            s = "1" + s

        return s