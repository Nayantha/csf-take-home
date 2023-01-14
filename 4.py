def display_words():
    with open("story.txt", "r") as text_file:
        for word in text_file.read().replace("\n", " ").split(" "):
            if len(word) < 4:
                print(word)


display_words()
