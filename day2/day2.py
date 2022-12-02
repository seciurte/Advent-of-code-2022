#!/bin/python3

INPUT_FILE = "input.txt"

OP_RPS		= {
	"A": 1,
	"B": 2,
	"C": 3
}
PL_RPS		= {
	"X": 1,
	"Y": 2,
	"Z": 3
}

PL_WIN_TO	= {
	OP_RPS["A"]: PL_RPS["Y"],
	OP_RPS["B"]: PL_RPS["Z"],
	OP_RPS["C"]: PL_RPS["X"],
}

WIN		= 6
DRAW	= 3
LOSE	= 0

def getPlayerScore(op, pl) :

	if (OP_RPS[op] == PL_RPS[pl]) :
		return DRAW + PL_RPS[pl]
	

def day2() :

	playerScore = 0
	for line in open("input.txt", "r") :
		playerScore += getPlayerScore(line.split()[0], line.split()[1])
	print(playerScore)

def	main() :
	day2()

if __name__ == "__main__" :
	main()