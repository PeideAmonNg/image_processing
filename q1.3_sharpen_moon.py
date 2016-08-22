from PIL import Image
import numpy
import random
import sys
import math

im = Image.open(sys.argv[1])

imarray = numpy.array(im)

def laplacianFilter():


	mask = [[0, -1, 0],
			[-1, 5, -1],
			[0, -1, 0]]

	outarray = [[0 for x in range(imarray.shape[1])] for y in range(imarray.shape[0])]



	i = 1
	while (i<imarray.shape[0]-1):
		j = 1
		while (j<imarray.shape[1]-1):
			total = (mask[0][0]*imarray[i-1][j-1] + mask[0][1]*imarray[i-1][j] + mask[0][2]*imarray[i-1][j+1]) + \
			(mask[1][0]*imarray[i][j-1] + mask[1][1]*imarray[i][j] + mask[1][2]*imarray[i][j+1]) + \
			(mask[0][0]*imarray[i+1][j-1] + mask[0][1]*imarray[i+1][j] + mask[0][2]*imarray[i+1][j+1]) 


			val = int(total)	

			if val < 0:
				val = 0

			if val > 255:
				val = 255

			outarray[i][j] = val

			j += 1

		i += 1

	out = Image.fromarray(numpy.asarray(outarray, dtype=numpy.uint8))
	out.save(sys.arg[2] + "-q1.3.png")
	print "laplacianFilter finished"

laplacianFilter()