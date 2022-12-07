import os

f = open("label.txt", "r")
lst=f.readlines()
for name in lst:
	os.mkdir(name[:-1])