class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        count: List[int] = [0] * n
        for i in range(n):
            for j in range(n):
                if nums[j] < nums[i]:
                    count[i] += 1
        return count
        