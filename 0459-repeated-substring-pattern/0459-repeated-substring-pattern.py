class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lastIndex = 0
        currentIndex = 1
        size = 1
        while size <= len(s)//2:
            current = s[lastIndex: currentIndex]
            
            lastIndex = currentIndex
            currentIndex = lastIndex + size
            while lastIndex <= len(s):
                if s[lastIndex: currentIndex] != current:
                    size += 1
                    lastIndex = 0
                    currentIndex = size
                    break
                else:
                    if currentIndex == len(s):
                        return True
                    lastIndex = currentIndex
                    currentIndex = lastIndex + size

            if currentIndex > len(s):
                size += 1
                lastIndex = 0
                currentIndex = size

        return False