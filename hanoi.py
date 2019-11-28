import time

def printTowers():
	for line in range(lines):
		print(''.join(tower1[line]) + ' ' + ''.join(tower2[line]) + ' ' + ''.join(tower3[line]))
	print('\n')
	return time.sleep(0.5)

def moveDisk(fr, to):
	row = []
	# Find first disk (from)
	for n in range(lines+1):
		if fr[n][middle] == '*':
			row = fr[n][:]
			delDisk(fr)
			break
	# Find first disk (to)
	for line in range(lines-1,-1,-1):
		if to[line][middle] == '|':
			# Add disk
			to[line] = row
			break
	return

def delDisk(tower):
	for n in range(lines):
		# Find Disk
		if tower[n][middle] == '*':
			# Empty Line
			for col in range(columns):
				tower[n][col] = ' '
			tower[n][middle] = '|'
			break
	return

def initHanoi():
	# Add all disks in first tower
	for line in range(lines):
		for n in range(line+1):
			tower1[line][middle-n] = '*'
			tower1[line][middle+n] = '*'
		tower2[line][middle] = "|"
		tower3[line][middle] = "|"
	return printTowers()

def solveHanoi(countDisk, tower1, tower2, tower3):
	if countDisk > 0:
		solveHanoi(countDisk - 1, tower1, tower3, tower2)
		moveDisk(tower1, tower3)
		printTowers()
		solveHanoi(countDisk - 1, tower2, tower1, tower3)
	else:
		return

countDisk = int(input("Nº Disks: "))		
lines = countDisk
columns = 2 * countDisk - 1
middle = countDisk - 1
# Towers
tower1 = [[' ' for x in range(columns)] for i in range(lines)]
tower2 = [[' ' for x in range(columns)] for i in range(lines)]
tower3 = [[' ' for x in range(columns)] for i in range(lines)]

initHanoi()
solveHanoi(countDisk, tower1, tower2, tower3)