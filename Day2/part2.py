def getOpponentMove(move):
	match move[0]:
		case 'A':
			return 1
		case 'B':
			return 2
		case 'C':
			return 3
		case _:
			return 0

def getMyMove(move, opponent):
	match move[0]:
		case 'X':
			match opponent:
				case 2:
					return 1
				case 3:
					return 2
				case 1:
					return 3
		case 'Y':
			return opponent
		case 'Z':
			match opponent:
				case 1:
					return 2
				case 2:
					return 3
				case 3:
					return 1
		case _:
			return 0

def scoreOfGame(opponent, me):
	if opponent == me:
		return 3

	if me == 1:
		return 6 * (opponent - 2)
	if me == 2:
		return 3 * (3 - opponent)
	if me == 3:
		return 6 * (opponent - 1)

	return 0
	


file = open("input.txt", "r")
lines = file.readlines()
file.close()

totalScore = 0

for line in lines:
	[opponentMoveStr, myMoveStr] = line.split(' ')

	opponentMove = getOpponentMove(opponentMoveStr)
	myMove = getMyMove(myMoveStr, opponentMove)

	winScore = scoreOfGame(opponentMove, myMove)

	totalScore += winScore + myMove

print(totalScore)

