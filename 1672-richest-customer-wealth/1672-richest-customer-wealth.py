class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxValue: int = 0;
        for i in accounts:
            currentMaxValue: int = sum(i)
            maxValue = max(maxValue, currentMaxValue)
        return maxValue
        