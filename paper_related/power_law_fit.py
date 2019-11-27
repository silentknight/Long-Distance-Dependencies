import numpy as np # This is the Numpy module
from scipy.optimize import curve_fit # The module that contains the curve_fit routine
import matplotlib.pyplot as plt # This is the matplotlib module which we use for plotting the result

""" Below is the function that returns the final y according to the conditions """
def fitfunc(x,a1,a2):
	xc = 2
	y1 = (x**(a1))[x<xc]
	y2 = (x**(a1-a2))[x>xc]
	y3 = (0)[x==xc]
	y = np.concatenate((y1,y2,y3))
	return y

x = np.array([0.001, 0.524, 0.625, 0.670, 0.790, 0.910, 1.240, 1.640, 2.180, 35460])
y = np.array([7.435e-13, 3.374e-14, 1.953e-14, 3.848e-14, 4.510e-14, 5.702e-14, 5.176e-14, 6.0e-14,3.049e-14,1.12e-17])

""" In the above code, we have imported 3 modules, namely Numpy, Scipy and matplotlib """

popt,pcov = curve_fit(fitfunc,x,y,p0=(10.0,1.0)) #here we provide random initial parameters a1,a2

a1 = popt[0] 
a2 = popt[1]
residuals = y - fitfunc(x,a1,a2)
chisq = sum( (residuals**2)/fitfunc(x,a1,a2) ) # This is the chi-square for your fitted curve

""" Now if you need to plot, perform the code below """
curvey = fitfunc(x,a1,a2) # This is your y axis fit-line

plt.plot(x, curvey, 'red', label='The best-fit line')
plt.scatter(x,y, c='b',label='The data points')
plt.legend(loc='best')
plt.show()