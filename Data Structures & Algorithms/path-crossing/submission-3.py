class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirc = {"N": [0, 1], "S": [0, -1], "W": [-1, 0], "E": [1, 0]}

        x = 0
        y = 0
        seen = {(x, y)}

        for p in path:
            dx, dy = dirc[p]
            x += dx
            y += dy
            if (x, y) in seen:
                return True

            seen.add((x, y))

        return False
