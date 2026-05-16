class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        res = -1
        for n in arr:
            if n == freq[n]:
                res = n

        return res
