#!/bin/python3

import re

INPUT_FILE = "input.txt"

def get_nb_columns() :

	for line in open(INPUT_FILE, "r") :
		tmp = line.split()[-1]
		if tmp.isdigit() :
			return int(tmp)

def do_move(move, stacks) :

	for crate in range(move["move"]) :
		tmp = stacks[move["from"]][-1]
		stacks[move["from"]].pop(-1)
		stacks[move["to"]].append(tmp)

def do_move_bonus(move, stacks) :

	len_stack_from = len(stacks[move["from"]])
	tmp = stacks[move["from"]][len_stack_from - move["move"]:len_stack_from]
	del stacks[move["from"]][len_stack_from - move["move"]:len_stack_from]
	stacks[move["to"]].extend(tmp)

def day5() :

	file = open(INPUT_FILE, "r")
	stacks = [[] for stack in range(get_nb_columns())]
	for line in file :
		if len(line) == 1 :
			break
		column = 0
		for index in range(1, len(line), 4) :
			if line[index].isalpha() :
				stacks[column].insert(0, line[index])
			column += 1
	for line in file :
		line = line.split()
		move = {
			line[0]: int(line[1]),
			line[2]: int(line[3]) - 1,
			line[4]: int(line[5]) - 1
		}
		do_move(move, stacks)
	for stack in stacks :
		print(stack[-1], end="")
	print()

def day5_bonus() :

	file = open(INPUT_FILE, "r")
	stacks = [[] for stack in range(get_nb_columns())]
	for line in file :
		if len(line) == 1 :
			break
		column = 0
		for index in range(1, len(line), 4) :
			if line[index].isalpha() :
				stacks[column].insert(0, line[index])
			column += 1
	for line in file :
		line = line.split()
		move = {
			line[0]: int(line[1]),
			line[2]: int(line[3]) - 1,
			line[4]: int(line[5]) - 1
		}
		do_move_bonus(move, stacks)
	for stack in stacks :
		if stack:
			print(stack[-1], end="")
	print()

if __name__ == "__main__" :
	day5()
	day5_bonus()