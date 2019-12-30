import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#Parallelogram vertices
D = np.array([8,0]) 
B = np.array([0,0]) 
C = np.array([6,4])
A = np.array([2,4]) 
E = np.array([3,2])
F = np.array([5,3.3])



#Generating all lines
x_AB = line_gen(A,B)
x_BD = line_gen(B,D)
x_DC = line_gen(D,C)
x_AC = line_gen(A,C)
x_AD = line_gen(A,D)
x_BC = line_gen(B,C)
x_AE = line_gen(A,E)
x_DF = line_gen(D,F)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AE[0,:],x_AE[1,:],label='$AE$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$DF$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


plt.show()
