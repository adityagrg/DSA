class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        prev = [1]
        ans.append(prev)

        for i in range(1, numRows):
            prevNum = 0
            newList = []
            for num in prev:
                newList.append(prevNum + num)
                prevNum = num
            
            newList.append(prevNum + 0)
            ans.append(newList)
            prev = newList
        
        return ans