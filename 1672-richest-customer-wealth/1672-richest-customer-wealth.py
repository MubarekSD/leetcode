class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxValue: int = 0;
        for i in accounts:
            maxValue = sum(i) if sum(i) > maxValue else maxValue
        return maxValue
        