# read the file
with open("test.txt", "r") as test_file:
    # readlines() read lines and append each line to a list
    # len gives the amount of elements in a list or equal iterable
    print("number of lines in the file: ",len(test_file.readlines()))
