class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cmap = Counter(arr)

        for s in arr:
            if cmap[s] == 1:
                k -= 1

            if k == 0:
                return s
        return ""
