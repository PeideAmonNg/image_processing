from PIL import Image
import numpy
import random
import sys
import math


im = Image.open(sys.argv[1])
# im.show()

sobel_x = [[-1, 0, 1],
			[-2, 0, 2],
			[-1, 0, 1]]

sobel_y = [[-1, -2, -1],
			[0, 0, 0],
			[1, 2, 1]]


imarray = numpy.array(im)
print imarray.shape

if len(sys.argv) != 3:
	raise Exception("Wrong arguments. Supply input and output files.")
outarray = [[0 for x in range(imarray.shape[1])] for y in range(imarray.shape[0])]

i = 1
while (i<imarray.shape[0]-1):
	j = 1
	while (j<imarray.shape[1]-1):
		pixel_x = (sobel_x[0][0]*imarray[i-1][j-1] + sobel_x[0][1]*imarray[i-1][j] + sobel_x[0][2]*imarray[i-1][j+1]) + \
		(sobel_x[1][0]*imarray[i][j-1] + sobel_x[1][1]*imarray[i][j] + sobel_x[1][2]*imarray[i][j+1]) + \
		(sobel_x[2][0]*imarray[i+1][j-1] + sobel_x[2][1]*imarray[i+1][j] + sobel_x[2][2]*imarray[i+1][j+1])

		pixel_y = (sobel_y[0][0]*imarray[i-1][j-1] + sobel_y[0][1]*imarray[i-1][j] + sobel_y[0][2]*imarray[i-1][j+1]) + (sobel_y[1][0]*imarray[i][j-1] + sobel_y[1][1]*imarray[i][j] + sobel_y[1][2]*imarray[i][j+1]) + (sobel_y[2][0]*imarray[i+1][j-1] + sobel_y[2][1]*imarray[i+1][j] + sobel_y[2][2]*imarray[i+1][j+1])

		val = int(math.sqrt(pixel_x*pixel_x + pixel_y*pixel_y))	

		if val < 0:
			val = 0

		if val > 255:
			val = 255

		outarray[i][j] = val

		j += 1

	i += 1

out = Image.fromarray(numpy.asarray(outarray, dtype=numpy.uint8))
out.save(sys.argv[2]+"-q1.1.png")
