#**********************************************************************#
# Title:                     Newton Raphson                            #
# Description :              This class is for Newton Raphson Method   #
# Author:                    Pfarelo Raliphada                         #
# Date:                      14 April 2021                             #
#**********************************************************************#

"""Implementation of Newton"""
# Raphson Method for solving equations

def func( x ):
	return x * x * x - x * x + 2

def derivFunc( x ):
	return 3 * x * x - 2 * x

""" Function to find the root"""
def newtonRaphson( x ):
""" Function to find the root"""
	h = func(x) / derivFunc(x)
	while abs(h) >= 0.0001:
		h = func(x)/derivFunc(x)
		
		# x(i+1) = x(i) - f(x) / f'(x)
		x = x - h
	
	print("The value of the root is : ", "%.4f"% x)


x0 = -20 
""" Initial values assumed """
newtonRaphson(x0)



