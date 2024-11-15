class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hm = set()
        for ch in sentence:
            hm.add(ch)
        
        for ch in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            if ch not in hm:
                return False
        
        return True
