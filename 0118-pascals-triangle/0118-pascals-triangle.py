class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for i in range(numRows - 1):
            temp = [0] + out[-1] + [0]
            row = []
            for j in range(len(out[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            out.append(row)
        return out