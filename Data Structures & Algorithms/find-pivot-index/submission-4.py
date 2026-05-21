class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += nums[i - 1] + prefix_sum[i - 1]

        for i in range(len(nums)):
            pre = prefix_sum[i]
            suf = prefix_sum[len(nums)] - prefix_sum[i + 1]

            if pre == suf:
                return i

        return -1
