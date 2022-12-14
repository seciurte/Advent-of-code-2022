#!/bin/python3

INPUT_FILE	= "input.txt"

IS_BEATEN	= {
	"rock": "paper",
	"paper": "scissors",
	"scissors": "rock"
}

OP_TO_RPS	= {
	"A": "rock",
	"B": "paper",
	"C": "scissors"
}

PL_TO_RPS	= {
	"X": "rock",
	"Y": "paper",
	"Z": "scissors"
}

PL_TO_WDL	= {
	"X": "lose",
	"Y": "draw",
	"Z": "win"
}

SCORES		= {
	"rock": 1,
	"paper": 2,
	"scissors": 3,
	"win": 6,
	"draw": 3,
	"lose": 0
}

def getPlayerScore(op, pl) :

	if OP_TO_RPS[op] == PL_TO_RPS[pl] :
		return SCORES["draw"] + SCORES[PL_TO_RPS[pl]]
	elif PL_TO_RPS[pl] == IS_BEATEN[OP_TO_RPS[op]] :
		return SCORES["win"] + SCORES[PL_TO_RPS[pl]]
	else :
		return SCORES["lose"] + SCORES[PL_TO_RPS[pl]]

def getPlayerScore_bonus(op, res) :

	for key in PL_TO_RPS.keys() :
		if SCORES[PL_TO_WDL[res]] == (getPlayerScore(op, key)) - SCORES[PL_TO_RPS[key]] :
			print("--- ", (getPlayerScore(op, key)) - SCORES[PL_TO_RPS[key]])
			return getPlayerScore(op, key)

def day2() :

	playerScore = 0
	for line in open("input.txt", "r") :
		playerScore += getPlayerScore(line.split()[0], line.split()[1])
	print(playerScore)

def day2_bonus() :

	playerScore = 0
	for line in open("input.txt", "r") :
		playerScore += getPlayerScore_bonus(line.split()[0], line.split()[1])
	print(playerScore)

if __name__ == "__main__" :
	day2()
	day2_bonus()