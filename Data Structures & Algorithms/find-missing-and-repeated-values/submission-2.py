class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [0] * 2
        count = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count[grid[i][j]] += 1

        for i in range(1, (len(grid) * len(grid)) + 1):
            if i not in count:
                res[1] = i

            if count[i] == 2:
                res[0] = i

        return res
