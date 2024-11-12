class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)

        sal = ""

        for i in range(n-1, -1, -1):
            if s[i].isalpha():
                sal += s[i]
        
        j = 0
        s_list = list(s)
        for i in range(n):
            if s_list[i].isalpha():
                s_list[i] = sal[j]
                j += 1
        
        ans = "".join(s_list)
        return ans
