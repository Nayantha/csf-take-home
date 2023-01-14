with open("Marks.txt") as marks_sheet:
    for student in marks_sheet.readlines():
        student = student.replace("\n", "").split(" ")
        name = student[0]
        sum = 0
        subjects = 0
        for mark in student[1:]:
            subjects += 1
            sum += int(mark)
        print(name, sum, sum / subjects)
    