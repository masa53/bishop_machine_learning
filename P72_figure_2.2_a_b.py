P72_figure_2.2_a_0.1_b_0.1


import numpy as np
from scipy import integrate
import matplotlib.pyplot as pyplot

#calcurate values of the gumma function

a=40;
b=25;

def pre_gamma_a(x):
    return ( x**(a-1.0)) * np.exp(-x)

def pre_gamma_b(x):
    return ( x**(b-1.0)) * np.exp(-x)

def pre_gamma_a_b(x):
    return ( x**(a+b-1.0)) * np.exp(-x)

g_a=integrate.quad(pre_gamma_a, 0, np.inf);
g_b=integrate.quad(pre_gamma_b, 0, np.inf);
g_a_b=integrate.quad(pre_gamma_a_b, 0, np.inf);

#plot beta function

def beta(x):
    return g_a_b[0]* ( (x)**(a-1.0) ) * ( (1.0-x)**(b-1.0)) /(g_a[0] * g_b[0])



px = np.arange(0.00001, 0.999999, 0.00001)

pyplot.xlim(0.0, 1.0)
pyplot.ylim(0.0, 10.0)
pyplot.title('Beta function a=40, b=25')
pyplot.xlabel('x')
pyplot.ylabel('y')

pyplot.plot(px, beta(px))
pyplot.show()




