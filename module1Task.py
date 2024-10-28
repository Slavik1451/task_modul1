grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
students_grades = {}
for i in range(len(grades)):
    grades_ = grades[i]
    students_grades[list_students[i]] = sum(grades_) / len(grades_)
print(students_grades)
