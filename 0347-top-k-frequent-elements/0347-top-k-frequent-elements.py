class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
        sorted_dict = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))

        i = 0
        ans = []
        for key in sorted_dict.keys():
            if i == k:
                break
            ans.append(key)
            i += 1
        return ans

