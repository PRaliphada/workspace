
#***********************************************************************************#
# Title:             Newton Raphson method                                          #
# Description:       This code is for Newton Raphson Methods (Numerical Analysis)   #
# Author:            Pfarelo Raliphada                                              #
# Date:              15 April 2021                                                  #
#***********************************************************************************#

def nraphson(fn, x, tol = 0.0001, maxiter = 100):
"""Returns the roots of an equation."""
    for i in range (maxiter): 
        xnew = x - fn[0](x)/fn[1](x)
        if abs (xnew -x) < tol: break
        x = xnew
    return xnew, i
    
y = [lambda x:  2*x**3 - 9.5*x + 7.5, lambda x:  6*x**2 - 9.5]

x, n = nraphson(y,5)

print("The root is %f at %d iterations." % (x, n))
