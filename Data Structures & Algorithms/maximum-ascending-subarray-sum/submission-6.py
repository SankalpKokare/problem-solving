class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        cur_count = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur_count += nums[i]
            else:
                cur_count = nums[i]

            res = max(res, cur_count)

        return res
