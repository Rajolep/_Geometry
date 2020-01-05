#Code by PRIYANKA R
#December 31, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import *

a = 3.5
b = 6.5

angD=(np.pi/180)*105
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angD))
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
ang=math.radians(60)
Q=np.array([0,0])
R=np.array([a,0])
P=np.array([p,q])

print(P)
A=np.array([-5.16,6.2375])
B=np.array([1.67905,6.27879])
D=np.array([-4.092196,9.0388])
an=np.tan((np.pi/180)*135)
#direction vector of PB
m1=np.array([1,an])
#normal vector of PB
n1 = np.matmul(omat,m1)
#Direction vector of PB = QB
m2=P-R
#normal vector of QB
n2 = np.matmul(omat,m2)
#print(n2)
#T = line_intersect(n1,A,n2,D)
N=np.vstack((n1,n2))
#print(n1,n2,N)
r = np.zeros(2)
r[0] = n1@P
r[1] = n2@Q
#print(r)
#Intersection
C=np.linalg.inv(N)@r
d=np.sqrt((C[0])**2+(C[1])**2)
angz=(np.pi/180)*75
e = np.sqrt(a**2+d**2-2*a*d*np.cos(angz))
p = (a**2 + e**2-d**2 )/(2*a)
q = np.sqrt(e**2-p**2)
print(e)

print(C)
#Generating all lines
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)
x_QP = line_gen(Q,P)
x_PC = line_gen(P,C)
x_QC = line_gen(Q,C)
x_AP = line_gen(A,P)
x_AQ = line_gen(A,Q)
x_AD = line_gen(A,D)
x_AC = line_gen(A,C)
x_DC = line_gen(D,C)
#Plotting all lines
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_QP[0,:],x_QP[1,:],label='$QP$')
plt.plot(x_PC[0,:],x_PC[1,:],label='$PC$')
plt.plot(x_QC[0,:],x_QC[1,:],label='$QC$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_AQ[0,:],x_AQ[1,:],label='$AQ$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.1), Q[1] * (1 - 0.1) , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 +0.1), R[1] * (1) , 'R')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.03), B[1] * (1 - 0.1) , 'B')
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





