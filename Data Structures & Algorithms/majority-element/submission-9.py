class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_count = 0
        res = -1

        for n in nums:
            if cur_count == 0:
                res = n

            cur_count += 1 if n == res else -1

        return res
