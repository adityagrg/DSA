class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nos = 0
        current = 0
        i = 0
        for current in range(1, arr[-1]):
            if arr[i] != current:
                nos += 1

                if nos == k:
                    return current
            else:
                i += 1
        
        return (current + 1 + k - nos)