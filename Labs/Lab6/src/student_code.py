import common

def part_one_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1

	weights = [0, 0, 0]
	learningRate = 0.01
	error = 1
	iterations = 1000
	
	# train
	while abs(error) > 0 or iterations > 0:

		error = 0
		for j in range(common.constants.TRAINING_SIZE):
			activation = weights[0] * data_train[j][0] + weights[1] * data_train[j][1] + weights[2]
			if activation >= 0:
				predicted = 1
			else:
				predicted = 0

			expected = data_train[j][2]
			delta = expected - predicted
			weights[0] += learningRate * delta * data_train[j][0]
			weights[1] += learningRate * delta * data_train[j][1]
			weights[2] += learningRate * delta
			error += delta

		iterations -= 1

	# classify
	for i in range(common.constants.TEST_SIZE):
		if weights[0] * data_test[i][0] + weights[1] * data_test[i][1] + weights[2] >= 0:
			data_test[i][2] = 1
		else:
			data_test[i][2] = 0

	return

def part_two_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8

	weights = [[0 for x in range(3)] for x in range(9)] 
	y = [0 for x in range(9)]
	learningRate = 0.01
	error = 1
	iterations = 1000

	while iterations > 0:

		error = 0
		# for each data sample
		for i in range(common.constants.TRAINING_SIZE):

			# calculate y values
			for w in range(9):
				y[w] = weights[w][0] * data_train[i][0] + weights[w][1] * data_train[i][1] + weights[w][2]
			argMax = max(y)
			predicted = y.index(argMax)
			expected = int(data_train[i][2])
			delta = predicted - expected

			if predicted != expected:
				weights[predicted][0] -= learningRate * data_train[i][0]
				weights[predicted][1] -= learningRate * data_train[i][1]
				weights[predicted][2] -= learningRate * weights[predicted][2] - 1

				weights[expected][0] += learningRate * data_train[i][0]
				weights[expected][1] += learningRate * data_train[i][1]
				weights[expected][2] += learningRate * weights[expected][2] + 1
				
			error += abs(predicted - expected)
		iterations -= 1

	for i in range(common.constants.TEST_SIZE):
		for w in range(9):
			y[w] = weights[w][0] * data_test[i][0] + weights[w][1] * data_test[i][1] + weights[w][2]
		argMax = max(y)
		predicted = y.index(argMax)
		data_test[i][2] = predicted

	return

# def done(weights, newWeights):
# 	for i in range(len(weights)):
# 		for j in range(3):
# 			if abs(weights[i][j] - newWeights[i][j]) > 0.01:
# 				return False
# 	return True