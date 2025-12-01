import os
import datetime

size = os.path.getsize("spider.txt")
print(size)
#This code will provide the file size

timestamp = os.path.getmtime("./spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
#This code will provide a unix timestamp for the file

abspath = os.path.abspath("spider.txt")
print(abspath)
#This code takes the file name and turns it into an absolute path