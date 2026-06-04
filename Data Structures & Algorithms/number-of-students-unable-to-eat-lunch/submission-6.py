class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total_stud = len(students)
        san_pref = Counter(students)

        for s in sandwiches:
            if san_pref[s] > 0:
                total_stud -= 1
                san_pref[s] -= 1
            else:
                break

        return total_stud
