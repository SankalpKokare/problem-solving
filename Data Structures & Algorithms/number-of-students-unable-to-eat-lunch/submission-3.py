class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total_students = len(students)
        sand_prefrence = Counter(students)

        for s in sandwiches:
            if sand_prefrence[s] > 0:
                total_students -= 1
                sand_prefrence[s] -= 1
            else:
                break

        return total_students
