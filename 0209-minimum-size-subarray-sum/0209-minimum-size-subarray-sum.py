class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        mini = float('inf')
        returnZero = True
        ptr1 = 0
        ptr2 = 0
        noOfElements = 0
        while True:
            if currentSum >= target:
                returnZero = False
                if noOfElements == 1:
                    return 1

                if noOfElements < mini:
                    mini = noOfElements

                noOfElements -= 1
                currentSum -= nums[ptr1]
                ptr1 += 1
                continue
            
            if ptr2 >= len(nums):
                break
            currentSum += nums[ptr2]
            ptr2 += 1
            noOfElements += 1

        if returnZero:
            return 0
        else:
            return mini