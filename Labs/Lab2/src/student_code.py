import common
def astar_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	
	start = (0, 0)
	goal = (0, 0)
	for x in range(0, common.constants.MAP_WIDTH-1):
		for y in range(0, common.constants.MAP_HEIGHT-1):
			if map[y][x] == 2:
				start = (y, x) 
			if map[y][x] == 3:
				goal = (y, x)

	# new, empty priority queue
	priorityQueue = PriorityQueue()
	predecessors = {}
	distFromStart = {}

	# add to priorityQueue, predecessors
	yStart, xStart = start
	predecessors[start] = None
	distFromStart[start] = 0
	startPriority = h(start, goal) # + distFromStart[start]
	priorityQueue.push(startPriority, (yStart, xStart))

	while (priorityQueue.len() > 0):
	 	y, x = priorityQueue.pop() 

	 	# Found the end!
		if map[y][x] == 3:
			map[y][x] == 5
			constructPath(predecessors, (y, x), map)
			map[yStart][xStart] = 5
			return True

		# Mark as visited and process children
		map[y][x] = 4
		if inRangeAndNotVisited(y - 1, x, map):
			currPoint = (y - 1, x)
			distFromStart[currPoint] = distFromStart[(y, x)] + 1
			p1 = distFromStart[currPoint] + h(currPoint, goal)
			priorityQueue.push(p1, currPoint)
			predecessors[currPoint] = (y, x) 
		if inRangeAndNotVisited(y, x - 1, map):
			currPoint = (y, x - 1)
			distFromStart[currPoint] = distFromStart[(y, x)] + 1
			p2 = distFromStart[currPoint] + h(currPoint, goal)
			priorityQueue.push(p2, currPoint)
			predecessors[currPoint] = (y, x) 
		if inRangeAndNotVisited(y + 1, x, map):
			currPoint = (y + 1, x)
			distFromStart[currPoint] = distFromStart[(y, x)] + 1
			p3 = distFromStart[currPoint] + h(currPoint, goal)
			priorityQueue.push(p3, currPoint)
			predecessors[currPoint] = (y, x) 
		if inRangeAndNotVisited(y, x + 1, map):
			currPoint = (y, x + 1)
			distFromStart[currPoint] = distFromStart[(y, x)] + 1
			p4 = distFromStart[currPoint] + h(currPoint, goal)
			priorityQueue.push(p4, currPoint)
			predecessors[currPoint] = (y, x) 

	return False

# heuristic function
def h(point, goal):
	yPoint, xPoint = point
	yGoal, xGoal = goal
	return abs(yPoint - yGoal) + abs(xPoint - xGoal)

# Check for in bounds and not already visited
def inRangeAndNotVisited(y, x, map):
	return (y >= 0 and y < common.constants.MAP_HEIGHT and x >= 0 and x < common.constants.MAP_WIDTH and (map[y][x] == 0 or map[y][x] == 3))

# Draw the path from the end to start
def constructPath(predecessors, currPoint, map):
	while(predecessors[currPoint] != None):
		currY, currX = currPoint
		map[currY][currX] = 5
		currPoint = predecessors[currPoint]
	return

# reinventing the wheel, but with worse performance 
class PriorityQueue(object):
	def __init__(self):
		self.priorityQueue = []

	def push(self, newPriority, newPoint):
		newY, newX = newPoint
		i = 0
		if not self.priorityQueue:
			self.priorityQueue.append((newPriority, newPoint))
			return
		else:
			for priority, point in self.priorityQueue:
				y, x = point
				# move right until you find a priority = or less
				if priority > newPriority:
					i += 1
					continue
				# you have a tie in priorities, sort first by x's then by y's
				elif priority == newPriority:
					# compare x's
					if x < newX:
						self.priorityQueue.insert(i, (newPriority, newPoint))
						return
					# if even the x's are equal
					elif x == newX:
						# compare the y's
						if y < newY:
							self.priorityQueue.insert(i, (newPriority, newPoint))
							return
					else:
						i += 1
						continue

				# the priority you uncountered is the min so far, so insert
				else: 
					self.priorityQueue.insert(i, (newPriority, newPoint))
					return
				i += 1
		# you have reached the end, and not inserted yet
		self.priorityQueue.append((newPriority, newPoint))

	def pop(self):
		p, point = self.priorityQueue.pop()
		return point

	def len(self):
		return len(self.priorityQueue)
