
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
#a = 6
#b = 4.5
#c = 7.5
a = 4
b = 6
angD = np.pi/180*85
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angD))

print(c)

#Coordinates of A
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)

#Parallelogram vertices
A = np.array([p,q]) 
D = np.array([0,0]) 
C = np.array([a,0]) 

#Mid point of BD
O =(A+D)/2
o=(1.75632,3)
#Finding A
B = 2*O-C
F= alt_foot(D,C,B)
print(F)
E=alt_foot(A,B,C)
print(E)

#Generating all lines
x_BD = line_gen(B,D)
x_DC = line_gen(D,C)
x_CB = line_gen(C,B)
x_AD = line_gen(A,D)
x_BA = line_gen(B,A)
x_CA = line_gen(C,A)
x_CD = line_gen(C,D)
x_BC = line_gen(B,C)
x_AE = line_gen(A,E)
x_DF = line_gen(D,F)
#Plotting all lines
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BA[0,:],x_BA[1,:],label='$BA$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
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
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')
plt.plot(o[0], o[1], 'o')
plt.text(o[0] * (1 + 0.03), o[1] * (1 - 0.1) , 'o')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/quad/pgm_sss.pdf')
#plt.savefig('./figs/quad/pgm_sss.eps')
#subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sss.pdf"))
#else
plt.show()








