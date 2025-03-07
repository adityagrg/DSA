class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}        
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in hm:
                return [hm[target - num], i]

            hm[nums[i]] = i
        
        return [-1, -1]