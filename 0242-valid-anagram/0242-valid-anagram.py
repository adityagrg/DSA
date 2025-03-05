class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}
        for ch in s:
            if ch in hms:
                hms[ch] += 1
            else:
                hms[ch] = 1
        
        for ch in t:
            if ch in hmt:
                hmt[ch] += 1
            else:
                hmt[ch] = 1
        
        for key, value in hms.items():
            if key not in hmt:
                return False
            else:
                if value == hmt[key]:
                    del hmt[key]
        
        if len(hmt) == 0:
            return True
        
        return False