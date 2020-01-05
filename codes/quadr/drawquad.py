#Code by PRIYANKA R
#December 31, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Sides
c = 5
d = 4.5
ang = 60*np.pi/180
b =  4
#Coordinates of D
p = np.sqrt(b**2+c**2-2*b*c*np.cos(ang))

x = (c**2 + b**2-p**2 )/(2*c)
y = np.sqrt(b**2-x**2)

print(x,y)

#QUAD vertices
D = np.array([x,y]) 
E = np.array([0,0]) 
A = np.array([c,0]) 
R = np.array([c,d])

#Generating all lines
x_DE = line_gen(D,E)
x_EA = line_gen(E,A)
x_AR = line_gen(A,R)
x_RD = line_gen(R,D)

#Plotting all lines
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EA[0,:],x_EA[1,:],label='$EA$')
plt.plot(x_AR[0,:],x_AR[1,:],label='$AR$')
plt.plot(x_RD[0,:],x_RD[1,:],label='$RD$')

plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 - 0.2), E[1] * (1) , 'E')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


plt.show()







