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

	# mark the start node as visited and add to queue, path
	yStart, xStart = start
	map[yStart][xStart] = 5
	queue.insert(0, (yStart, xStart))
	predecessors[start] = None

	while (len(queue) > 0):
		y, x = queue.pop() 
		print "value = ", map[y][x]

		if map[y][x] == 3:
			map[y][x] == 5
			point = (y, x)
			print "before constructPath"
			constructPath(predecessors, point, map)
			return True

		if inRangeAndNotVisited(y, x + 1, map):
			if map[y][x + 1] != 3:
				map[y][x + 1] = 4
			queue.insert(0, (y, x + 1))
			predecessors[(y, x + 1)] = (y, x)
		if inRangeAndNotVisited(y + 1, x, map):
			if map[y + 1][x] != 3:
				map[y + 1][x] = 4
			queue.insert(0, (y + 1, x))
			predecessors[(y + 1, x)] = (y, x)
		if inRangeAndNotVisited(y, x - 1, map):
			if map[y][x - 1] != 3:
				map[y][x - 1] = 4
			queue.insert(0, (y, x - 1))
			predecessors[(y, x - 1)] = (y, x) 
		if inRangeAndNotVisited(y - 1, x, map):
			if map[y - 1][x] != 3:
				map[y - 1][x] = 4
			queue.insert(0, (y - 1, x))
			predecessors[(y - 1, x)] = (y, x) 

	return False

def inRangeAndNotVisited(y, x, map):
	return (y >= 0 and y < common.constants.MAP_HEIGHT-1 and x >= 0 and x < common.constants.MAP_WIDTH-1 and (map[y][x] == 0 or map[y][x] == 3))

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

# breadth first
# queue = []
# queue.insert(0, item)
# queue.pop()

# First [y][x+1], then [y+1][x], then [y][x-1], and finally [y-1][x]