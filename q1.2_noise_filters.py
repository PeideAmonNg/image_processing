from PIL import Image
import numpy
import random
import sys
import math

im = Image.open(sys.argv[1])

imarray = numpy.array(im)

def medianFilter():

	outarray = [[0 for x in range(imarray.shape[1])] for y in range(imarray.shape[0])]

	i = 1
	while (i<imarray.shape[0]-1):
		j = 1
		while (j<imarray.shape[1]-1):
			median = numpy.median([imarray[i-1][j-1], imarray[i-1][j], imarray[i-1][j+1], imarray[i][j-1], imarray[i][j], imarray[i][j+1], imarray[i+1][j-1], imarray[i+1][j], imarray[i+1][j+1]])

			outarray[i][j] = median

			j += 1

		i += 1

	out = Image.fromarray(numpy.asarray(outarray, dtype=numpy.uint8))
	out.save(sys.argv[2] + "-q1.2-medianFilter.png")
	print "medianFilter finished"

def meanFilter():

	e = float(1)/9

	mask = [[e, e, e],
			[e, e, e],
			[e, e, e]]

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
	out.save(sys.argv[2] + "-q1.2-mean.png")
	print "meanFilter finished"


medianFilter()
meanFilter()