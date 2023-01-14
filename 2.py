CONTENT_STR = "'Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'"
CONTENT_LIST = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

with open("2-str-version.txt", "w") as text_file:
    text_file.write(CONTENT_STR)

with open("2-list-version.txt", "w") as text_file:
    for i in CONTENT_LIST[:-1:]:
        text_file.write(i + "\n")  # move next element to new line
    text_file.write(CONTENT_LIST[-1])  # last item with out moving the cursor to next new line
    