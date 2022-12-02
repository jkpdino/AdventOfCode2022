
# Read the lines from the file
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

currCalories = 0
topThree = [ 0, 0, 0 ]

for line in lines:
	if str.isspace(line):
		topThree.append(currCalories)
		topThree.sort(reverse=True)
		topThree.pop()
		currCalories = 0
	else:
		currCalories += int(line)

topThree.append(currCalories)
topThree.sort(reverse=True)
topThree.pop()


print(topThree[0] + topThree[1] + topThree[2])