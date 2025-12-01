file = open("spider.txt")

#The readline() method reads one line from the file and returns it as a string.
print(file.readline())

# The read() method reads the entire file and returns it as a string.
print(file.read())

# The close() method closes the file.
file.close()

#The line that uses the with statement to open the file spider.txt is in read mode. The as keyword assigns the file object to the variable file. The code block inside the with statement will be executed, and then the file will be closed automatically.  
with open("spider.txt") as file:
    print(file.readline())