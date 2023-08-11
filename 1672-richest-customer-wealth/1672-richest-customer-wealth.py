class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxMo = 0
        for customer in accounts:
            sum = 0
            for m in customer:
                sum += m
            maxMo = max(maxMo, sum)
        return maxMo
        