class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        res = [0] * 2
        count = defaultdict(int)

        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        for i in range(1, (n * n) + 1):
            if count[i] == 0:
                res[1] = i
            elif count[i] == 2:
                res[0] = i

        return res
