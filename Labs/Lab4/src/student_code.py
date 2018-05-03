import common

class variables:
	counter=0

# -------------------- backtracking ---------------------- #

def sudoku_backtracking(sudoku):
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter = 0
	recur_backtrack(sudoku)
	return variables.counter

def recur_backtrack(sudoku):
	if assignmentComplete(sudoku):
		return True
	i, j = getNextAssigned(sudoku)
	for value in range(1, 10):
		if fitsConstraints(sudoku, i, j, value):
			variables.counter += 1
			sudoku[i][j] = value
			result = recur_backtrack(sudoku)
			if result == True:
				return result
			sudoku[i][j] = 0
	return False

# ----------------- forward checking --------------------- #

def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	variables.counter+=1000000
	return variables.counter

def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	variables.counter+=1000000
	return variables.counter

def assignmentComplete(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				return False
	return True

def getNextAssigned(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				return i, j
	return False

def fitsConstraints(sudoku, y, x, z):
	for i in range(9):
		if (sudoku[y][i]==z):
			return False
		if (sudoku[i][x]==z):
			return False
		if(sudoku[(y/3)*3+i/3][(x/3)*3+i%3]==z): 
			return False
	return True