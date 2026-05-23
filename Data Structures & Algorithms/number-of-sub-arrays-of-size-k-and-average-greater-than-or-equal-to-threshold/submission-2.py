class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        threshold *= k
        res = cursum = 0

        for r in range(len(arr)):
            cursum += arr[r]
            if r >= k - 1:
                res += cursum >= threshold
                cursum -= arr[r - k + 1]

        return res
