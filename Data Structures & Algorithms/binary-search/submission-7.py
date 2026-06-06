class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums) - 1, nums, target)

    def bs(self, l, r, nums, target):
        if l > r:
            return -1

        m = l + (r - l) // 2

        if nums[m] == target:
            return m

        if nums[m] > target:
            return self.bs(l, m - 1, nums, target)
        else:
            return self.bs(m + 1, r, nums, target)
