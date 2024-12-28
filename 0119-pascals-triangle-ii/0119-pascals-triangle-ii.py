class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]

        for i in range(0, rowIndex):
            newList = []
            prevNum = 0

            for num in prev:
                newList.append(prevNum + num)
                prevNum = num
            
            newList.append(prevNum + 0)
            del prev
            prev = newList

        return prev