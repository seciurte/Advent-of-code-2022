#!/bin/python3

INPUT_FILE	= "input.txt"

def addDir(path, dirSizes, dir) :

	if dir == ".." :
		path.pop(-1)
	else:
		path.append(dir)
		dirSizes[dir] = 0

def updateDirSizes(path, dirSizes, size) :

	for dir in path :
		dirSizes[dir] += size

def day7() :

	dirSizes	= {}
	path		= []
	file		= open(INPUT_FILE, "r")
	res			= 0

	for line in file :
		line = line.split()
		if "cd" in line :
			addDir(path, dirSizes, line[2])
		elif not "ls" in line and not "dir" in line :
			updateDirSizes(path, dirSizes, int(line[0]))
	file.close()

	for size in dirSizes.values() :
		if size <= 100000 :
			res += size

	for dir, size in dirSizes.items() :
		if size <= 100000 :
			print(dir, ":", size)
	# print(res)

if __name__ == "__main__" :

	day7()