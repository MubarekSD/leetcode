class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(n - 1):
                if "{}".format(nums[j]) + "{}".format(nums[j + 1]) < "{}".format(nums[j + 1]) + "{}".format(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if nums[0] == 0:
            return '0'
        else:
            return ''.join(map(str, nums))
        