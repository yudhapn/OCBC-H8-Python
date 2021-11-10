try:
    file = open('Hack8_Sample_Text.txt', 'w', encoding = 'utf-8')
    file.write("my first file\n")
    file.write("This file\n\n")
    file.write("contains three lines\n")
finally:
    file.close()

try:
    file = open('Hack8_Sample_Text.txt', 'r', encoding = 'utf-8')
    file.seek(0)   # bring file cursor to initial position
    for line in file:
        print(line, end = '')

    with open('Hack8_Sample_Text.txt', 'r') as reader:
     # Read & print the entire file
        print(reader.read())
finally:
    file.close()