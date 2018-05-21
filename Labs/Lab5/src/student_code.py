import common

def drone_flight_planner (map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# 

	# 70, 15, 15, 0 regular
	# 80, 10, 10, 0 
	# start: 1, end: 2, enemy: 3

	# fill up policies, values, 
	# battery drop cost is cost for each move without out turbo, turbo doubles it
	# discount per cycle is gamma

	# return expected utility, converge within 0.1%
	# south, west, north, east search order

	# V_k+1 (s) = max over all a -> sum over all next states (t(s,a,s')) (R(s,a,s') + gamma * V_k(s')) 

	return droneFlightPlannerRecur(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, 1 - discount_per_cycle)

def droneFlightPlannerRecur(map, policies, values, deliveryFee, batteryDropCost, dronerepairCost, discountPerCycle):

	oldValues = [row[:] for row in values]

	for i in range(6):
		for j in range(6):
			currState = (i, j)
			bestPolicy, bestValue = maxActionReward(map, policies, oldValues, deliveryFee, batteryDropCost, dronerepairCost, discountPerCycle, currState)
			values[i][j] = bestValue
			policies[i][j] = bestPolicy

	if done(values, oldValues):
		return valueOfStart(map, values)
	else:
		return droneFlightPlannerRecur(map, policies, values, deliveryFee, batteryDropCost, dronerepairCost, discountPerCycle)


# returns sum of rewards for each action from a currState
def maxActionReward(map, policies, values, deliveryFee, batteryDropCost, dronerepairCost, discountPerCycle, currState):
	rewards = {}
	i, j = currState

	rewards[common.constants.SOFF] = \
		((.7 * (reward(map, i + 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i + 1, j, batteryDropCost))) 
		+ (.15 * (reward(map, i, j + 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j + 1, batteryDropCost))) 
		+ (.15 * (reward(map, i, j - 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j - 1, batteryDropCost)))) 

	rewards[common.constants.WOFF] = \
		((.7 * (reward(map, i, j - 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j - 1, batteryDropCost))) 
		+ (.15 * (reward(map, i + 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i + 1, j, batteryDropCost))) 
		+ (.15 * (reward(map, i - 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i - 1, j, batteryDropCost)))) 
	
	rewards[common.constants.NOFF] = \
		((.7 * (reward(map, i - 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i - 1, j, batteryDropCost))) 
		+ (.15 * (reward(map, i, j + 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j + 1, batteryDropCost))) 
		+ (.15 * (reward(map, i, j - 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j - 1, batteryDropCost))))

	rewards[common.constants.EOFF] = \
		((.7 * (reward(map, i, j + 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j + 1, batteryDropCost))) 
		+ (.15 * (reward(map, i + 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i + 1, j, batteryDropCost))) 
		+ (.15 * (reward(map, i - 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i - 1, j, batteryDropCost))))

	batteryDropCost *= 2

	rewards[common.constants.SON] = \
		((.8 * (reward(map, i + 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i + 1, j, batteryDropCost))) \
		+ (.1 * (reward(map, i, j + 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j + 1, batteryDropCost))) \
		+ (.1 * (reward(map, i, j - 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j - 1, batteryDropCost)))) 

	rewards[common.constants.WON] = \
		((.8 * (reward(map, i, j - 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j - 1, batteryDropCost))) \
		+ (.1 * (reward(map, i + 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i + 1, j, batteryDropCost))) \
		+ (.1 * (reward(map, i - 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i - 1, j, batteryDropCost)))) 

	rewards[common.constants.NON] = \
		((.8 * (reward(map, i - 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i - 1, j, batteryDropCost))) \
		+ (.1 * (reward(map, i, j + 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j + 1, batteryDropCost))) \
		+ (.1 * (reward(map, i, j - 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j - 1, batteryDropCost)))) 

	rewards[common.constants.EON] = \
		((.8 * (reward(map, i, j + 1, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i, j + 1, batteryDropCost))) \
		+ (.1 * (reward(map, i + 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i + 1, j, batteryDropCost))) \
		+ (.1 * (reward(map, i - 1, j, deliveryFee, batteryDropCost, dronerepairCost) + discountPerCycle * value(values, i - 1, j, batteryDropCost)))) 

	# batteryDropCost /= 2
	maxPolicy, maxValue = max(rewards.iteritems(), key=lambda x:x[1])
	return (maxPolicy, maxValue)

def reward(map, i, j, deliveryFee, batteryDropCost, dronerepairCost):
	# if you bouce off the wall, no reward
	if outOfBounds(i, j):
		return -batteryDropCost
	# if you hit an enemy, must pay to move there and repair
	if map[i][j] == common.constants.RIVAL:
		return -(dronerepairCost + batteryDropCost)
	# if you found the end, pay to move but reap rewards
	if map[i][j] == common.constants.CUSTOMER:
		return  (deliveryFee - batteryDropCost)
	# just a normal space or pizza space
	else:
		return (-batteryDropCost)
	
def value(values, i, j, batteryDropCost):
	if outOfBounds(i, j):
		return -batteryDropCost
	else:
		return values[i][j]

def done(values, newValues):
	for i in range(6):
		for j in range(6):
			if abs(values[i][j] - newValues[i][j]) > .01:
				return False
	return True

def valueOfStart(map, values):
	for i in range(6):
		for j in range(6):
			if map[i][j] == common.constants.PIZZA:
				return values[i][j]

def outOfBounds(i, j):
	return i < 0 or i > 5 or j < 0 or j > 5

		
