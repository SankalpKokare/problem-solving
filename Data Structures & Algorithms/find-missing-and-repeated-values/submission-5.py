class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)
        res = [0] * 2

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        for i in range(1, (n * n) + 1):
            if count[i] == 2:
                res[0] = i
            if count[i] == 0:
                res[1] = i

        return res
