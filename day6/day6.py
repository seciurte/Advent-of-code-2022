#!/bin/python3

INPUT_FILE = "input.txt"

def isMaker(str) :

	for c in str :
		if str.count(c) > 1 :
			return False
	return True

def day6() :

	line = open(INPUT_FILE, "r").readline()
	for index in range(len(line) - 4) :
		if isMaker(line[index: index + 4]) :
			print(index + 4)
			return

def day6_bonus() :

	line = open(INPUT_FILE, "r").readline()
	for index in range(len(line) - 14) :
		if isMaker(line[index: index + 14]) :
			print(index + 14)
			return

if __name__ == "__main__" :
	day6()
	day6_bonus()