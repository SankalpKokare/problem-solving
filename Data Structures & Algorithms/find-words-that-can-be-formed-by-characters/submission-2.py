class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_C = Counter(chars)
        res = 0

        for w in words:
            w_count = Counter(w)
            add = True
            for c in w:
                if w_count[c] > total_C[c]:
                    add = False
                    break
            if add:
                res += len(w)

        return res
