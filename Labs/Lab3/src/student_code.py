import common

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	
	result = common.game_status(board);

	# terminal state, someone winning
	if result == common.constants.X or result == common.constants.O:
		return result
	# terminal state, tie
	if result == common.constants.NONE and boardFull(board):
		return result

	# otherwise, keep playing
	if turn == common.constants.X:
		return maxX(board)
	if turn == common.constants.O:
		return maxO(board)

def maxO(board):
	# set not to -inf, because X is worst you can do
	v = common.constants.X
	for i, space in enumerate(board):
		# if the space is empty, you can put an O there
		if space == common.constants.NONE:
			board[i] = common.constants.O
			v = max_o(v, minmax_tictactoe(board, common.constants.X))
			board[i] = common.constants.NONE
	return v

def maxX(board):
	# set not to inf, because O is worst you can do
	v = common.constants.O
	for i, space in enumerate(board):
		# if the space is empty, you can put an X there
		if space == common.constants.NONE:
			board[i] = common.constants.X
			v = max_x(v, minmax_tictactoe(board, common.constants.O))
			board[i] = common.constants.NONE
	return v

# helper to test for ties vs. not done
def boardFull(board):
	for space in board:
		if space == common.constants.NONE:
			return False
	return True

# both named max because they are both just trying to max themselves winning
def max_x(v, minmax):
	if v == common.constants.X or minmax == common.constants.X:
		return common.constants.X
	if v == common.constants.NONE or minmax == common.constants.NONE:
		return common.constants.NONE
	return common.constants.O

def max_o(v, minmax):
	if v == common.constants.O or minmax == common.constants.O:
		return common.constants.O
	if v == common.constants.NONE or minmax == common.constants.NONE:
		return common.constants.NONE
	return common.constants.X


def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return common.constants.NONE
