import common
import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line = common.Line()
	hough = common.init_space(2000, 2000)

	# go over image
	for y in range(common.constants.HEIGHT):
		for x in range (common.constants.WIDTH):

			if ((image[0][y][x] == 0) and (image[1][y][x] == 0) and (image[2][y][x] == 0)):

				for m_graph in range(0, 2000):
					m = float(m_graph) / float(100) - 10
					b = -(m * x) + y
					if (b > -1000 and b < 1000):
						hough[m_graph][int(b) + 1000] += 1

	maximum = -1

	# find max in hough space
	for y in range(2000):
		for x in range(2000):
			if hough[y][x] > maximum:
				maximum = hough[y][x]
				m = float(y) / 100 - 10
				b = x - 1000.4

	line.m = m
	line.b = b
		
	return line

def detect_normal(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.theta and line.r
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	hough = common.init_space(1800, 1800)


	# go over image
	for y in range(common.constants.HEIGHT):
		for x in range (common.constants.WIDTH):

			if ((image[0][y][x] == 0) and (image[1][y][x] == 0) and (image[2][y][x] == 0)):

				for theta_graph in range(0, 1800):
					theta = math.radians(float(theta_graph) / float(10))
					r = x * math.cos(theta) - y * math.sin(theta)
					if (r > -900 and r < 900):
						hough[theta_graph][int(r) + 900] += 1

	maximum = -1

	# find max in hough space
	for y in range(1800):
		for x in range(1800):
			if hough[y][x] > maximum:
				maximum = hough[y][x]
				theta = math.pi - math.radians(float(y) / float(10))
				r = 900 - x
	line.r = r
	line.theta = theta

	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	numCircles = 0
	radius = 30.0
	radiusSquared = 30.0 * 30.0

	newImage = common.init_space(480, 640)
	hough = common.init_space(480, 640)

	# make edge detection greyscale image
	newImage, maxGradient = sobel(image, newImage)

	# normalize the image
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			newImage[y][x] = (newImage[y][x] / maxGradient) * 255

	# find the circles in hough space
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if newImage[y][x] == 255:
				for a in range(640):
					if (x - a)**2 < radiusSquared:
						b = float(y) - math.sqrt(radiusSquared - float((x - a)**2))
						if 0.0 < b and b < 480.0:
							hough[int(b)][a] += 1 

	# find number of circles
	for y in range(480):
		for x in range(640):
			if hough[y][x] > 32:
				numCircles += 1

	return numCircles

def sobel(image, newImage):

	maxGradient = 0

	for y in range(1, common.constants.HEIGHT - 1):
		for x in range(1, common.constants.WIDTH - 1):

			Dx = 0.0
			Dy = 0.0

			intensity = (image[0][y - 1][x - 1] + image[1][y - 1][x - 1] + image[2][y - 1][x - 1]) / 3

			Dx += -intensity
			Dy += -intensity

			intensity = (image[0][y][x - 1] + image[1][y][x - 1] + image[2][y][x - 1]) / 3

			Dx += -2 * intensity

			intensity = (image[0][y + 1][x + 1] + image[1][y + 1][x + 1] + image[2][y + 1][x + 1]) / 3

			Dx += -intensity
			Dy += intensity

			intensity = (image[0][y - 1][x] + image[1][y - 1][x] + image[2][y - 1][x]) / 3

			Dy += -2 * intensity

			intensity = (image[0][y + 1][x] + image[1][y + 1][x] + image[2][y + 1][x]) / 3

			Dy += 2 * intensity

			intensity = (image[0][y - 1][x + 1] + image[1][y - 1][x + 1] + image[2][y - 1][x + 1]) / 3

			Dx += intensity
			Dy += -intensity

			intensity = (image[0][y][x - 1] + image[1][y][x - 1] + image[2][y][x - 1]) / 3

			Dx += 2 * intensity

			intensity = (image[0][y + 1][x + 1] + image[1][y + 1][x + 1] + image[2][y + 1][x + 1]) / 3

			Dx += intensity
			Dy += intensity

			gradient = math.sqrt(Dx * Dx + Dy * Dy)
			maxGradient = max(maxGradient, gradient)
			newImage[y][x] = gradient

	return newImage, maxGradient
