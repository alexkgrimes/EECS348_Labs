import common

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	
	result = common.game_status(board);

	# if the state is a terminal state: 
	# 	return the state’s utility
	# if the next agent is MAX: 
	# 	return max-value(state)
	# if the next agent is MIN: 
	# 	return min-value(state)

	return common.constants.NONE

	def max-value(state):
		initialize v = -∞
		for each successor of state:
			v = max(v, value(successor))
		return v

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return common.constants.NONE
