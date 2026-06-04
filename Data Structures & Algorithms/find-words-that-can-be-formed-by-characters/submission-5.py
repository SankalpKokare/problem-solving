class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countC = Counter(chars)
        res = 0

        for w in words:
            c_count = Counter(w)
            add = True
            for c in w:
                if c not in countC:
                    add = False
                    break
                if countC[c] < c_count[c]:
                    add = False
                    break
            if add:
                res += len(w)

        return res
