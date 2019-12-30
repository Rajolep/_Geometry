import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


b=5
c=3
a=np.sqrt(b**2-c**2)

L = np.array([0,a]) 
M = np.array([0,0]) 
N = np.array([c,0]) 

print(a)
 
 

#Generating all lines
x_LM = line_gen(L,M)
x_MN = line_gen(M,N)
x_NL = line_gen(N,L)


#Plotting all lines
plt.plot(x_LM[0,:],x_LM[1,:],label='$LM$')
plt.plot(x_MN[0,:],x_MN[1,:],label='$MN$')
plt.plot(x_NL[0,:],x_NL[1,:],label='$NL$')


plt.plot(L[0], L[1], 'o')
plt.text(L[0] * (1 + 0.1), L[1] * (1 - 0.1) , 'L')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 - 0.2), M[1] * (1) , 'M')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 + 0.03), N[1] * (1 - 0.1) , 'N')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
