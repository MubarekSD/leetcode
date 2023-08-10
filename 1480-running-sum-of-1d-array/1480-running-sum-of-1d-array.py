class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i + 1):
                sum += nums[j]
            out.append(sum)
        return out