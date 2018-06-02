import common
import math

import matplotlib.pyplot as plt

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

	for y in range(2000):
		for x in range(2000):
			if hough[y][x] > maximum:
				maximum = hough[y][x]
				m = float(y)/100-10
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
	line.r=0
	line.theta=0
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	return 0

# def draw_graph():
# 	plt.plot(, l_accuracy)
# 	plt.show()
# 				