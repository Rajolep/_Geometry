#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Drawing a parallelogram  given 2 sides and a diagonal
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *





a = 3
b = 5
angP = np.pi/180*105
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angP))

print(c)

#Coordinates of P
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)
#Coordinates of C
f = 8
ang = np.pi/180*75
g = np.sqrt(f**2+c**2-2*f*c*np.cos(ang))
print(g)
p1 = (c**2 + f**2-g**2 )/(2*c)
q1 = np.sqrt(f**2-p1**2)
print(p1,q1)
#Parallelogram vertices
P = np.array([p,q]) 
Q = np.array([0,0]) 
R = np.array([a,0]) 
C = np.array([p1,q1]) 
#Mid point of BD
O =(Q+P)/2
#Finding B
B = 2*O-R
A=np.array([-(5-B[0]),(B[1])])
h = 5
i=3
angB = np.pi/180*105
j = np.sqrt(h**2+i**2-2*h*i*np.cos(angB))
print(j)
O1 = (A+C)/2
D = 2*O1-B

print(P)
print(B)
print(C)
print(D)
print(A)

#Generating all lines

x_QR = line_gen(Q,R)
x_PQ = line_gen(P,Q)
x_BP = line_gen(B,P)
x_PR = line_gen(P,R)
x_QC = line_gen(Q,C)
x_CP = line_gen(C,P)
x_BA = line_gen(B,A)
x_QA = line_gen(Q,A)
x_AC = line_gen(A,C)
x_AD = line_gen(A,D)
x_DC = line_gen(D,C)
#Plotting all lines

plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_BP[0,:],x_BP[1,:],label='$BP$')
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
plt.plot(x_QC[0,:],x_QC[1,:],label='$QC$')
plt.plot(x_CP[0,:],x_CP[1,:],label='$CP$')
plt.plot(x_BA[0,:],x_BA[1,:],label='$BA$')
plt.plot(x_QA[0,:],x_QA[1,:],label='$QA$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(-3.7,4.82)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B(1.29,4.82)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q(0,0)')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R(3,0)')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P(4.29,4.82)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(2.07,7.72)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D(-2.92,7.72)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/quad/pgm_sss.pdf')
plt.savefig('../../figs/quadexer.eps')
plt.show()







