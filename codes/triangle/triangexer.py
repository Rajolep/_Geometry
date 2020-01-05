#Code by PRIYANKA R
#December 31, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import *


#if using termux
#import subprocess
#import shlex
#end if


#Triangle sides
#a = 6
#b = 4.5
#c = 7.5
a = 3.5
b = 6.5

angD=(np.pi/180)*105
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angD))
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
ang=math.radians(60)
D=np.array([0,0])
C=np.array([a,0])
A=np.array([p,q])
O=np.array([3.05,3.7])
print(A)

an=np.tan((np.pi/180)*135)
#direction vector of AB
m1=np.array([1,an])
#normal vector of AB
n1 = np.matmul(omat,m1)
#Direction vector of AB = DB
m2=A-C
#normal vector of DB
n2 = np.matmul(omat,m2)
#print(n2)
#T = line_intersect(n1,A,n2,D)
N=np.vstack((n1,n2))
#print(n1,n2,N)
r = np.zeros(2)
r[0] = n1@A
r[1] = n2@D
#print(r)
#Intersection
B=np.linalg.inv(N)@r
d=np.sqrt((B[0])**2+(B[1])**2)
angz=(np.pi/180)*75
e = np.sqrt(a**2+d**2-2*a*d*np.cos(angz))
p = (a**2 + e**2-d**2 )/(2*a)
q = np.sqrt(e**2-p**2)
print(e)
F= alt_foot(D,C,B)
print(F)
E=alt_foot(A,B,C)
print(E)


#Generating all lines
x_DC = line_gen(D,C)
x_CA = line_gen(C,A)
x_DA = line_gen(D,A)
x_AB = line_gen(A,B)
x_DB = line_gen(D,B)
x_CB = line_gen(C,B)
x_CF = line_gen(F,C)
x_AE = line_gen(A,E)
x_DF = line_gen(D,F)
#Plotting all lines
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB$')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')
plt.plot(x_AE[0,:],x_AE[1,:],label='$AE$')
plt.plot(x_DF[0,:],x_DF[1,:],label='$DF$')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 +0.1), C[1] * (1) , 'C')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.03), B[1] * (1 - 0.1) , 'B')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.03), O[1] * (1 - 0.1) , 'O')
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





