# #Here there are spaces between the lines in the output. This is because there is a new line character at the end of each line. 
with open("spider.txt") as file:
    for line in file:
        print(line.upper())

# #Strip is used to remove the newline character, and we get the output without empty lines.
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())


#Here, the lines have been sorted alphabetically, so they're no longer in the order that they were in the file. We can see that Python displays a newline character using "\n" symbol when printing a list of strings. This is a way of explicitly showing that there's a new line character in those strings. This displays a character that's not printable, Python uses escape sequences with backslash, like \n. Another common escape sequence is \t, for tab.
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)