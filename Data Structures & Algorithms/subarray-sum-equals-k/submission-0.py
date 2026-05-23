class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cusum = 0
        prefixSum = {0: 1}

        for n in nums:
            cusum += n
            diff = cusum - k

            res += prefixSum.get(diff, 0)
            prefixSum[cusum] = 1 + prefixSum.get(cusum, 0)

        return res
