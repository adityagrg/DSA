class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0
        pointer = 0
        ans = 0

        while (pointer < len(nums)):
            if (nums[pointer] != val):
                nums[first] = nums[pointer]
                first += 1
                ans += 1

            pointer += 1
        
        return ans