import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

#input params
b = 5 # baselength
h = 3 #altitude
angA = 70 #angle made by the base and one side

temp_vec = np.array([h / np.tan(np.pi / 180 * angA), 0])
height_vec = np.array([0, h])

#Quad vertices
A = np.array([0, 0])
B =  A + np.array([b, 0])
C = B - temp_vec + height_vec
D = A + temp_vec + height_vec

#foot of perpendicular
P1 = A + temp_vec
P2 = B - temp_vec

print(A, D, B, C)
print(P1,P2)

#Generating all lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_DC = line_gen(D, C)
x_AD = line_gen(A, D)
x_DP1 =  line_gen(D, P1)
x_CP2 =  line_gen(C, P2)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_DC[0,:], x_DC[1,:], label='$DC$')
plt.plot(x_AD[0,:], x_AD[1,:], label='$AD$')
#for perpendicular
# plt.plot(x_DP1[0,:], x_DP1[1,:], linestyle='dotted', label='$DP1$')
# plt.plot(x_CP2[0,:], x_CP2[1,:], linestyle='dotted', label='$CP2$')

plt.plot(A[0], A[1], 'o')
plt.text(-0.2, 0.05, 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.02), B[1], 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 + 0.05) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.1), D[1] * (1 + 0.05) , 'D')
#labelling the foot of perpendicular
# plt.plot(P1[0], P1[1], 'o')
# plt.text(P1[0] * (1 + 0.03), -0.2 , 'P1')
# plt.plot(P2[0], P2[1], 'o')
# plt.text(P2[0] * (1 + 0.03), -0.2 , 'P2')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

#if using termux
# plt.savefig('./figs/trapezium.eps')
# plt.savefig('./figs/trapezium.eps')
# subprocess.run(shlex.split("termux-open ./figs/trapezium.eps"))
#else
plt.show()
