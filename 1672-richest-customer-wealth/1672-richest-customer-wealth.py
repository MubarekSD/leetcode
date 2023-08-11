class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxValue: int = 0;
        for i in accounts:
            maxValue = max(maxValue, sum(i))
        return maxValue
        