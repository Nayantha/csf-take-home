TEXT = "Mary had a little lamb, \n" \
       "Little lamb, little lamb, \n" \
        "Mary had a little lamb, \n"  \
        "Its fleece was white as snow, \n" \
        "And everywhere that Mary went, \n" \
        "Mary went, Mary went, \n" \
        "Everywhere that Mary went, \n" \
        "The lamb was sure to go;"

# write to the file
with open("test.txt", "w") as test_file:
    test_file.writelines(TEXT)
    
#read the file
with open("test.txt", "r") as test_file:
    print(test_file.read())
