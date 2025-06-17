import numpy as np
from math import floor, log10
import matplotlib.pyplot as plt

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial 
    at x
    '''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

def newtonrap (polyno,appx):

    dev=polyno.deriv()
    x=appx-(polyno(appx)/dev(appx))

    return x

def error (curr, prev):

    per=np.sqrt((((curr-prev)/curr)*100)**2)

    return per

def round_3sf (x):

    return round(x,-int(floor(log10(abs(x))))+2)

#the list of value of x, y and t
t = np.array([0,2.85,5.69,8.54,11.38,14.22])
x = np.array([0,202.78,391.66,569.87,738.45,896.31])
y= np.array([0,164.61,240.99,235.75,153.53,0])

# get the divided difference coef
a_s = divided_diff(t, x)[0,:]
a2_s= divided_diff(t, y)[0,:]
b_s = divided_diff(t, x)
b2_s= divided_diff(t, y)

# evaluate on new data points
t_new = np.arange(0, 17, .5)
x_new = newton_poly(a_s, t, t_new)
y_new = newton_poly(a2_s, t, t_new)

# plotting the x graphs
plt.figure(figsize = (12, 8))
plt.plot(t, x, 'bo')
plt.plot(t_new, x_new)
#plt.show()

# plotting the y graph
plt.figure(figsize = (12, 8))
plt.plot(t, y, 'bo')
plt.plot(t_new, y_new)
plt.show()

# generating the newton polynomial 
print("newton polynomial for x is", a_s)
print("newton polynomial for y is", a2_s)

#generating polynomial coefficient of the best fit line in the most appropriate degree
numy=np.polyfit(t_new , y_new, len(y)-1)

#y displacement equation generated
dip=np.poly1d(numy)

#y velocity equation generated
vel=dip.deriv()

#let the first guess be 6
first=6

#newton raphson method until error less or equal to 0.05%
while True:
    q=newtonrap(vel,first)
    r=error(q,first)

    #the result is in 3 significant figures
    print(round_3sf(q), "error is", r, "%")

    #the iterative process stops as error becomes equal or lesser than 0.05%
    if (r<=0.05):
       break 
    else:
        first=q
        continue

#generating polynomial coefficient of the best fit line in the most appropriate degree
numx=np.polyfit(t_new , x_new, len(x)-1)

#x displacement equation generated
dip2=np.poly1d(numx)

#x velocity equation generated
vel2=dip2.deriv()

#x velocity at apogee at 3 significant figures
print("horizontal velocity at apogee is", round_3sf(vel2(q)))


