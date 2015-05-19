#!/usr/bin/python

import numpy as np
from scipy.fftpack import fftn, ifftn
from PIL import Image
import sys

def toMat(src, row, col) :
	dest = np.zeros((row, col, 3))
	for i in range(dest.shape[0]) :
		for j in range(dest.shape[1]) :
			dest[i][j][0] = src[i,j][0]
			dest[i][j][1] = src[i,j][1]
			dest[i][j][2] = src[i,j][2]
	return dest

def toImg(src, dest, row, col) :
#	img = Image.new( 'RGB', (src.shape[0],src.shape[1]), "black" ) 
#	dest = img.load() 
	for i in range(row) :
		for j in range(col) :
			t = (int(src[i][j][0]), int(src[i][j][1]), int(src[i][j][2]))
			dest[i,j] = t

def cond1(m, i, j, maxi, maxj, k) :
	return m[i][j][k] < 20

def cond2(m, i, j, maxi, maxj, k) :
	return i > maxi - 20 and j > maxj - 20

def cond3(m, i, j, maxi, maxj, k) :
	return i < 100 and j < 100

def cond4(m, i, j, maxi, maxj, k) :
	return i < 100

def cond5(m, i, j, maxi, maxj, k) :
	return j < 100
	
def cond6(m, i, j, maxi, maxj, k) :
	return m[i][j][k] > 100


def filt(m) :
	for i in range(m.shape[0]) :
		for j in range(m.shape[1]) :
			for k in range(m.shape[2]) :
				if cond5(m, i, j, m.shape[0], m.shape[1], k) :
					m[i][j][k] = 0


img = Image.open(sys.argv[2])
pixels = img.load() # create the pixel map

x = toMat(pixels, img.size[0], img.size[1])
y = fftn(x)

filt(y)

yinv = ifftn(y)
res = np.absolute(yinv)
toImg(res, pixels, img.size[0], img.size[1])

img.save(sys.argv[1] + sys.argv[2])
