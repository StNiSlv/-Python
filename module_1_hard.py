grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = sorted(students)
sr_arifm0 = [float(sum(grades[0])/len(grades[0])), float(sum(grades[1])/len(grades[1])), float(sum(grades[2])/len(grades[2])), float(sum(grades[3])/len(grades[3])), float(sum(grades[4])/len(grades[4]))]
print(students_)
average_student_scores = {students_[0]:sr_arifm0[0], students_[1]:sr_arifm0[1], students_[2]:sr_arifm0[2],students_[3]:sr_arifm0[3], students_[4]:sr_arifm0[4]}
print(average_student_scores)
print(average_student_scores.__sizeof__())