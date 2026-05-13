class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i in range(len(nums)):
            suf_sum = prefix_sum[len(nums)] - prefix_sum[i + 1]

            if prefix_sum[i] == suf_sum:
                return i

        return -1
