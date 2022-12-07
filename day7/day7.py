#!/bin/python3

INPUT_FILE	= "input.txt"

def addDir(path, dirSizes, dir) :

	if dir == ".." :
		path.pop(-1)
	else :
		path.append(dir)
		dirSizes[dir] = 0

def updateDirSizes(path, dirSizes, file) :

	

def day7() :

	dirSizes = {}
	path = []
	file = open(INPUT_FILE, "r")

	for line in file :
		line = line.split()
		if line[0] == "$" :
			if line[1] == "cd" :
				addDir(path, dirSizes, line[2])
			else :
				updateDirSizes(path, dirSizes, file)
if __name__ == "__main__" :

	day7()