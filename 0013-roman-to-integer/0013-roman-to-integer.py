class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == 'I':
                if (i < len(s) - 1) and (s[i+1] != 'X') and (s[i+1] != 'V'):
                    ans += 1
                elif (i < len(s) - 1) and (s[i+1] == 'X'):
                    ans += 9
                    i += 1
                elif (i < len(s) - 1) and (s[i+1] == 'V'):
                    ans += 4
                    i += 1
                else:
                    ans += 1
            elif c == 'X':
                if (i < len(s) - 1) and (s[i+1] != 'L') and (s[i+1] != 'C'):
                    ans += 10
                elif (i < len(s) - 1) and (s[i+1] == 'L'):
                    ans += 40
                    i += 1
                elif (i < len(s) - 1) and (s[i+1] == 'C'):
                    ans += 90
                    i += 1
                else:
                    ans += 10
            elif c == 'C':
                if (i < len(s) - 1) and (s[i+1] != 'D') and (s[i+1] != 'M'):
                    ans += 100
                elif (i < len(s) - 1) and (s[i+1] == 'D'):
                    ans += 400
                    i += 1
                elif (i < len(s) - 1) and (s[i+1] == 'M'):
                    ans += 900
                    i += 1
                else:
                    ans += 100
            elif c == 'V':
                ans += 5
            elif c == 'L':
                ans += 50
            elif c == 'D':
                ans += 500
            elif c == 'M':
                ans += 1000
            else:
                print("Error")
            i += 1
        
        return ans