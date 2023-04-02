class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ret = []
        n = len(nums)
        for i in range(n):
            for j in range(n - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            
        for i in range(n):
            if nums[i] == target:
                ret.append(i)
        return ret
        