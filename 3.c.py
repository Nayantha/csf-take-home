print("input pattern: name marks1 marks2 marks3 marks4")
while True:
    text = input("Enter name and marks: ")
    if text.lower() == "exit":
        break
    with open("Marks.txt", "a") as marks_file:
        marks_file.write(text + "\n")
    