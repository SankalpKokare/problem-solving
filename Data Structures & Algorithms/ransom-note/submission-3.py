class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ran = Counter(ransomNote)
        count_mag = Counter(magazine)

        for r in ransomNote:
            if count_mag[r] < count_ran[r]:
                return False

        return True
