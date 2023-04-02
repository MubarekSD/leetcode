class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        out = [[1]]
        for i in range(rowIndex):
            temp = [0] + out[-1] + [0]
            row = []
            for j in range(len(out[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            out.append(row)
        return out[rowIndex]