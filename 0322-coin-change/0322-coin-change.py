class Solution:
    def _util(self, coins, amount, hm):
        if amount in hm:
            return hm[amount]

        if amount < 0:
            return -1

        possible = 0
        current_min = float('inf')
        for coin in coins:
            value = self._util(coins, (amount - coin), hm)
            if value != -1:
                possible = 1
                if value + 1 < current_min:
                    current_min = value + 1
        
        if possible == 1:
            hm[amount] = current_min
        else:
            hm[amount] = -1
        
        return hm[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)

        hm = {}
        hm[0] = 0
        return self._util(coins, amount, hm)