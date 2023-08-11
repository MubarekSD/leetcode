class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = []
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            out.append(sum)
        return (max(out))
        