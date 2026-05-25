class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cur_count = 0

        for n in nums:
            if cur_count == 0:
                res = n

            cur_count += 1 if res == n else -1

        return res
