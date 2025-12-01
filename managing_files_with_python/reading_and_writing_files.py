# “r” means open for reading, and “t” tells Python to expect a text file.
with open("sample_data/declaration.txt", "rt") as textfile:
    for line in textfile:
        print(line)

f = open("sample_data/declaration.txt", "w")

f = open("sample_data/declaration.txt", "w", encoding="utf-8")

f.close()

