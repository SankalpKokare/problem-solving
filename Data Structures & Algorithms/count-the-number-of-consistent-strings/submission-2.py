class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allow = set(allowed)
        res = 0

        for w in words:
            add = True
            for c in w:
                if c not in allow:
                    add = False
                    break
            if add:
                res += 1

        return res
