#!/bin/python3
import string

INPUT_FILE	= "input.txt"

alph = list(string.ascii_lowercase) + list(string.ascii_uppercase)

def day3() :

	prioScore = 0
	for line in open(INPUT_FILE, "r") :
		c = [c1 for c1 in line[:int(len(line)/2)] if c1 in line[int(len(line)/2):]]
		prioScore += alph.index(c[0]) + 1
	print(prioScore)

def day3_bonus() :

	prioScore = 0
	with open(INPUT_FILE, "r") as file :
		lines = file.readlines()
		for i in range(0, len(lines), 3) :
			set1, set2, set3 = set(lines[i]), set(lines[i + 1]), set(lines[i + 2])
			c = [x for x in list((set1 & set2 & set3)) if x != "\n"]
			prioScore += alph.index(c[0]) + 1
	print(prioScore)

if __name__ == "__main__" :
	day3()
	day3_bonus()