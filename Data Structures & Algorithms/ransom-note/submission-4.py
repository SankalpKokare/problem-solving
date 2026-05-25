class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for k in countR:
            if countR[k] > countM[k]:
                return False
        return True
