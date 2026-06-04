class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 1
        n = len(nums)

        for i in range(1, n * 2):
            if nums[(i % n) - 1] <= nums[i % n]:
                count += 1
            else:
                count = 1

            if count == n:
                return True

        return n == 1
