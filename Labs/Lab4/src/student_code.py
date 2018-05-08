import common

class variables:
	counter=0

# -------------------- backtracking ---------------------- #

def sudoku_backtracking(sudoku):
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter = 0
	unassignedVars = initUnassignedVarsBack(sudoku)
	recurBacktrack(unassignedVars, sudoku)
	return variables.counter

def recurBacktrack(unassignedVars, sudoku):
	variables.counter += 1
	if not unassignedVars:
		return True
	i, j = unassignedVars.pop(0)

	# for each value in the domain
	for value in range(1, 10):
		if fitsConstraints(sudoku, i, j, value):
			sudoku[i][j] = value
			result = recurBacktrack(unassignedVars, sudoku)
			if result == True:
				return result
			sudoku[i][j] = 0
	unassignedVars.insert(0, (i, j))
	return False

# ----------------- forward checking --------------------- #

def sudoku_forwardchecking(sudoku):
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter = 0
	# map (y,x) -> list of possible values
	unassignedVars = initUnassignedVarsForward(sudoku)
	varList = initVarList(sudoku)
	recurForwardCheck(sudoku, unassignedVars, varList)
	return variables.counter

def recurForwardCheck(sudoku, unassignedVars, varList):
	variables.counter += 1

	# all vars have been assigned
	if not varList:
		return True

	# get current variable, with corresponding values
	currVar = varList.pop(0)
	i, j = currVar
	values = unassignedVars[currVar]
	unassignedVars.pop(currVar)

	# for each value in the domain
	for value in values:
		sudoku[i][j] = value
		copyUnassignedVars = copyDict(unassignedVars)
		if not removeInconsistentValues(sudoku, copyUnassignedVars, currVar):
			result = recurForwardCheck(sudoku, copyUnassignedVars, varList)
			if result == True:
				return result
		sudoku[i][j] = 0

	# undo the pop's at the beginning
	varList.insert(0, (i, j))
	unassignedVars[currVar] = values
	return False

def removeInconsistentValues(sudoku, unassignedVars, currVar):
	removed = False
	curri, currj = currVar
	for var, values in unassignedVars.iteritems():
		i, j = var
		# if the currVar assignment would affect you
		if i == curri or j == currj or inSameSquare(var, currVar):
			for value in unassignedVars[var]:
				if not fitsConstraints(sudoku, i, j, value):
					unassignedVars[var].remove(value)
				if not unassignedVars[var]:
					removed = True
	return removed


# ------------------------ MRV --------------------------- #

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

# ------------------ helpers ----------------------------- #

def fitsConstraints(sudoku, y, x, z):
	for i in range(9):
		if (sudoku[y][i]==z):
			return False
		if (sudoku[i][x]==z):
			return False
		if(sudoku[(y/3)*3+i/3][(x/3)*3+i%3]==z): 
			return False
	return True

def initUnassignedVarsBack(sudoku):
	unassignedVars = []
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				unassignedVars.append((i, j))
	return unassignedVars

def initUnassignedVarsForward(sudoku):
	unassignedVars = {}
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				unassignedVars[(i, j)] = []
	# only add possible values that fit fixed constraints
	for point, values in unassignedVars.iteritems():
		i, j = point
		for k in range(1, 10):
			if fitsConstraints(sudoku, i, j, k):
				values.append(k)
	return unassignedVars

def initVarList(sudoku):
	varList = []
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				varList.append((i, j))
	return varList

def inSameSquare(var, currVar):
	i, j = var
	curri, currj = currVar
	return i / 3 * 3 + j / 3 == curri / 3 * 3 + currj

def copyDict(dictionary):
	newDict =  {}
	for key in dictionary:
		newDict[key] = []
	for key, values in dictionary.iteritems():
		for val in values:
			newDict[key].append(val)
	return newDict

	