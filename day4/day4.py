#!/bin/python3

import re

INPUT_FILE = "input.txt"

def day4() :

	nbPairs = 0
	for line in open(INPUT_FILE, "r") :
		ranges = [int(i) for i in re.findall(r"[\w']+", line)]
		if (
			(ranges[0] >= ranges[2] and ranges[1] <= ranges[3])
			or (ranges[2] >= ranges[0] and ranges[3] <= ranges[1])
		) :
			nbPairs += 1
	print(nbPairs)

def day4_bonus() :

	nbPairs = 0
	for line in open(INPUT_FILE, "r") :
		ranges = [int(i) for i in re.findall(r"[\w']+", line)]
		if (
			(ranges[0] >= ranges[2] and ranges[0] <= ranges[3])
			or (ranges[1] >= ranges[2] and ranges[1] <= ranges[3])
			or (ranges[2] >= ranges[0] and ranges[2] <= ranges[1])
			or (ranges[3] >= ranges[0] and ranges[3] <= ranges[1])
		) :
			nbPairs += 1
	print(nbPairs)

if __name__ == "__main__" :
	day4()
	day4_bonus()