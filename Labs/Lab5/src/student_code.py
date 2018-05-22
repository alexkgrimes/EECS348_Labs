import common

def drone_flight_planner(map, policies, values, deliveryFee, batteryDropCost, dronerepairCost, discountPerCycle):
	# PUT YOUR CODE HERE
	# V_k+1 (s) = max over all a -> sum over all next states (t(s,a,s')) (R(s,a,s') + gamma * V_k(s')) 

	discountPerCycle = 1 - discountPerCycle
	actions = [common.constants.SOFF, common.constants.WOFF, common.constants.NOFF, common.constants.EOFF, common.constants.SON, common.constants.WON, common.constants.NON, common.constants.EON]
	states = [common.constants.SOUTH, common.constants.WEST, common.constants.NORTH, common.constants.EAST]
	directions = [[1,0], [0,-1], [-1,0], [0,1]]

	# initialize RIVAL and CUSTOMER spaces
	for i in range(6):
		for j in range(6):
			if map[i][j] == common.constants.RIVAL:
				values[i][j] = -dronerepairCost
				policies[i][j] = common.constants.EXIT
			if map[i][j] == common.constants.CUSTOMER:
				values[i][j] = deliveryFee
				policies[i][j] = common.constants.EXIT

	while True:
		# cache old values 
		oldValues = [row[:] for row in values]
		oldPolicies = [row[:] for row in policies]

		# loop over all positions in the map
		for i in range(6):
			for j in range(6):
				maxValue = float('-inf')
				if map[i][j] != common.constants.RIVAL and map[i][j] != common.constants.CUSTOMER:	

					# loop over all actions
					for action in actions:
						value = 0
						
						# loop over all next states
						for state in states:
							iPrime = i + directions[state - 1][0]
							jPrime = j + directions[state - 1][1]

							transition = T(iPrime, jPrime, i, j, action)
							reward = R(action, batteryDropCost)

							# the usual case
							if not outOfBounds(iPrime, jPrime):
								value += transition * (reward + discountPerCycle * oldValues[iPrime][jPrime])
							# othewise, bounce off the wall
							else:
								if iPrime < 0:
									value += transition * (reward + discountPerCycle * oldValues[i][jPrime])
								if iPrime > 5:
									value += transition * (reward + discountPerCycle * oldValues[i][jPrime])
								if jPrime < 0:
									value += transition * (reward + discountPerCycle * oldValues[iPrime][j])
								if jPrime > 5:
									value += transition * (reward + discountPerCycle * oldValues[iPrime][j])

						# find max over all actions	
						if value > maxValue:
							maxValue = value
							policies[i][j] = action
							values[i][j] = maxValue

		# if converged, break, otherwise keep iterating
		if valuesDone(oldValues, values) and policiesDone(oldPolicies, policies):
			break

	return valueOfStart(map, values)

def R(action, batteryDropCost):
	if action == common.constants.NOFF or action == common.constants.EOFF or action == common.constants.WOFF or action == common.constants.SOFF:
		return -batteryDropCost
	if action == common.constants.NON or action == common.constants.EON or action == common.constants.WON or action == common.constants.SON:
		return -(2 * batteryDropCost)

def T(iPrime, jPrime, i, j, action):
	if action == common.constants.SOFF:
		if iPrime == i + 1:
			return 0.7
		if jPrime == j + 1 or jPrime == j - 1:
			return 0.15

	if action == common.constants.WOFF:
		if jPrime == j - 1:
			return 0.7
		if iPrime == i + 1 or iPrime == i - 1:
			return 0.15

	if action == common.constants.NOFF:
		if iPrime == i - 1:
			return 0.7
		if jPrime == j + 1 or jPrime == j - 1:
			return 0.15

	if action == common.constants.EOFF:
		if jPrime == j + 1:
			return 0.7
		if iPrime == i + 1 or iPrime == i - 1:
			return 0.15

	if action == common.constants.SON:
		if iPrime == i + 1:
			return 0.8
		if jPrime == j + 1 or jPrime == j - 1:
			return 0.1
	
	if action == common.constants.WON:
		if jPrime == j - 1:
			return 0.8
		if iPrime == i + 1 or iPrime == i - 1:
			return 0.1

	if action == common.constants.NON:
		if iPrime == i - 1:
			return 0.8
		if jPrime == j + 1 or jPrime == j - 1:
			return 0.1

	if action == common.constants.EON:
		if jPrime == j + 1:
			return 0.8
		if iPrime == i + 1 or iPrime == i - 1:
			return 0.1

	return 0.0

def valuesDone(values, newValues):
	for i in range(6):
		for j in range(6):
			if abs(values[i][j] - newValues[i][j]) > .001:
				return False
	return True

def policiesDone(policies, newPolicies):
	for i in range(6):
		for j in range(6):
			if policies[i][j] != newPolicies[i][j]:
				return False
	return True

def valueOfStart(map, values):
	for i in range(6):
		for j in range(6):
			if map[i][j] == common.constants.PIZZA:
				return values[i][j]

def outOfBounds(i, j):
	return i < 0 or i > 5 or j < 0 or j > 5



		
