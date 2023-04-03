class Solution:
    def sortList(self, stones: List[int]) -> List[int]:
        length = len(stones)
        for i in range(length):
            for j in range(length - 1):
                if stones[j] > stones[j + 1]:
                    stones[j], stones[j + 1] = stones[j + 1], stones[j]
        return stones
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) >= 2):
            self.sortList(stones)
            temp = stones[-1] - stones[-2]
            stones.remove(stones[-1])
            stones.remove(stones[-1])
            stones.append(temp)

        return stones[0]