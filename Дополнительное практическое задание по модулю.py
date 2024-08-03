grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
sr_arifm0 = float(sum(grades[0])/len(grades[0]))
sr_arifm1 = float(sum(grades[1])/len(grades[1]))
sr_arifm2 = float(sum(grades[2])/len(grades[2]))
sr_arifm3 = float(sum(grades[3])/len(grades[3]))
sr_arifm4 = float(sum(grades[4])/len(grades[4]))
print(students)
slovar_dly_teacher = {students[4]:sr_arifm0, students[1]:sr_arifm1, students[0]:sr_arifm2, students[3]:sr_arifm3, students[2]:sr_arifm4}
print(set(slovar_dly_teacher))