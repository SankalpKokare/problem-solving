class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allow = set(allowed)
        res = 0
        for w in words:
            add = True
            for i in range(len(w)):
                if w[i] not in allow:
                    add = False
                    break

            if add:
                res += 1
        return res
