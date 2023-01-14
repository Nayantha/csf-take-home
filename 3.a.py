print("enter exit at any time to exit the program.")
mark_sheet = {}  # { "student" : [ marks ] }
while False:  # change flag to run this snippet
    name = input("Enter name: ")
    if name.lower().replace(" ", "") == "exit":
        break
    marks = input("Enter marks separate them by a space: ")
    if marks.lower().replace(" ", "") == "exit":
        break
    marks_list = [mark for mark in marks.split(" ") if mark.isnumeric()]
    mark_sheet[name] = marks_list

# with open("Marks.txt", "w") as text_file:
#     for key, value in mark_sheet.items():
#         text_file.writelines(key + " " + " ".join(value) + " \n")


# take 2
print("input pattern: name marks1 marks2 marks3 marks4")
while True:
    text = input("Enter name and marks: ")
    if text.lower() == "exit":
        break
    with open("Marks.txt", "a") as marks_file:
        marks_file.write(text + "\n")
