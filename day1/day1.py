#!/bin/python3

INPUT_FILE	= "input.txt"

def day1() :

	calories = 0
	maxCalories = 0
	for line in open(INPUT_FILE, "r") :
		if (line == "\n") :
			maxCalories = max(calories, maxCalories)
			calories = 0
		else :
			calories += int(line)
	print(maxCalories)

def day1_bonus() :

	calories = 0
	allCalories = []
	for line in open(INPUT_FILE, "r") :
		if (line == "\n") :
			allCalories.append(calories)
			calories = 0
		else :
			calories += int(line)
	allCalories.sort()
	print(sum(allCalories[-3:]))

if __name__ == "__main__" :
	day1()
	day1_bonus()