import common
def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

def bf_search(map):
	found = False;
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	start = (0, 0)
	for x in range(0, common.constants.MAP_WIDTH-1):
		for y in range(0, common.constants.MAP_HEIGHT-1):
			if map[y][x] == 2:
				start = (y, x) 

	# new, empty queue
	queue = []
	predecessors = {}

	# add to queue, path
	yStart, xStart = start
	queue.insert(0, (yStart, xStart))
	predecessors[start] = None

	while (len(queue) > 0):
		y, x = queue.pop() 

		# Found the end!
		if map[y][x] == 3:
			map[y][x] == 5
			constructPath(predecessors, (y, x), map)
			map[yStart][xStart] = 5
			return True

		# Mark as visited and process children
		map[y][x] = 4
		if inRangeAndNotVisited(y, x + 1, map):
			queue.insert(0, (y, x + 1))
			predecessors[(y, x + 1)] = (y, x)
		if inRangeAndNotVisited(y + 1, x, map):
			queue.insert(0, (y + 1, x))
			predecessors[(y + 1, x)] = (y, x)
		if inRangeAndNotVisited(y, x - 1, map):
			queue.insert(0, (y, x - 1))
			predecessors[(y, x - 1)] = (y, x) 
		if inRangeAndNotVisited(y - 1, x, map):
			queue.insert(0, (y - 1, x))
			predecessors[(y - 1, x)] = (y, x) 

	return False

# Check for in bounds and not already visited
def inRangeAndNotVisited(y, x, map):
	return (y >= 0 and y < common.constants.MAP_HEIGHT and x >= 0 and x < common.constants.MAP_WIDTH and (map[y][x] == 0 or map[y][x] == 3))

# Draw the path from the end to start
def constructPath(predecessors, currPoint, map):
	print "constructPath"
	print "end point: ", currPoint
	while(predecessors[currPoint] != None):
		print "contructing the path"
		currY, currX = currPoint
		map[currY][currX] = 5
		currPoint = predecessors[currPoint]
	return




# depth first
# stack = []
# stack.append()
# stack.pop()

# First [y][x+1], then [y+1][x], then [y][x-1], and finally [y-1][x]