import common

# --------------- NORMAL MINMAX ------------------- #
def minmax_tictactoe(board, turn):
	
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

# -------------------- MINMAX WITH AB PRUNING ----------------------# 
def abprun_tictactoe(board, turn):
	# just return the helper because need to pass alpha and beta around
	return abprun_helper(board, turn, -1, -1)

def abprun_helper(board, turn, alpha, beta):
	result = common.game_status(board);

	# alpha is worst so far for O
	alpha = common.constants.X
	# beta is worst so far for X
	beta = common.constants.O

	# terminal state, someone winning
	if result == common.constants.X or result == common.constants.O:
		return result
	# terminal state, tie
	if result == common.constants.NONE and boardFull(board):
		return result

	# otherwise, keep playing
	if turn == common.constants.X:
		return maxAbX(board, alpha, beta)
	if turn == common.constants.O:
		return maxAbO(board, alpha, beta)

def maxAbO(board, alpha, beta):
	# set not to -inf, because X is worst you can do
	v = common.constants.X
	for i, space in enumerate(board):
		# if the space is empty, you can put an O there
		if space == common.constants.NONE:
			board[i] = common.constants.O
			v = max_o(v, abprun_helper(board, common.constants.X, alpha, beta))
			board[i] = common.constants.NONE
			# if v is better than beta, return (prune)
			if v == max_o(v, beta):
				return v
			alpha = max_o(alpha, v)
	return v

def maxAbX(board, alpha, beta):
	# set not to inf, because O is worst you can do
	v = common.constants.O
	for i, space in enumerate(board):
		# if the space is empty, you can put an X there
		if space == common.constants.NONE:
			board[i] = common.constants.X
			v = max_x(v, abprun_helper(board, common.constants.O, alpha, beta))
			board[i] = common.constants.NONE
			# if v is better than alpha, return (prune)
			if v == max_x(v, alpha):
				return v
			beta = max_x(beta, v)
	return v

# ------------------ communal helpers ---------------------#
# both named max because they are both just trying to max themselves winning
# use for both normal minmax and with ab pruning
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

# helper to test for ties vs. not done
def boardFull(board):
	for space in board:
		if space == common.constants.NONE:
			return False
	return True