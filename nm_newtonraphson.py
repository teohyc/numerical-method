import numpy as np
from math import floor, log10

def newtonrap (polyno,appx):

    dev=polyno.deriv()

    x=appx-(polyno(appx)/dev(appx))

    return x

def error (curr, prev):

    per=np.sqrt((((curr-prev)/curr)*100)**2)

    return per

def round_3sf (x):

    return round(x,-int(floor(log10(abs(x))))+2)

a=np.array([1.08e-04, -3.98e-03, 9e-02, -6, 74.2, -4.53e-13])
first=6

#getting displacement equation
dip=np.poly1d(a)

#getting velocity equation
vel=dip.deriv()

#newton raphson method until error less or equal to 0.05%
while True:
    x=newtonrap(vel,first)
    y=error(x,first)

    #the result is in 3 significant figures
    print(round_3sf(x), "error is", y, "%")

    if (y<=0.05):
       break 
    else:
        first=x
        continue

