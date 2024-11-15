class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        currentCount = nextCount = 0

        prevCh = s[0]
        counter = 1
        elements = []
        for i in range(1, len(s)):
            ch = s[i]
            if ch == prevCh:
                counter += 1
            else:
                elements.append(counter)
                counter = 1
                prevCh = ch
        
        elements.append(counter)

        if len(elements) < 2:
            return 0
        
        ans = 0
        for i in range(0, len(elements) - 1):
            ans += min(elements[i], elements[i + 1])
        
        return ans