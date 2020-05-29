import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex

#Sides
ac = 5
ad = 5
length_of_bis = 6

#Angles
angA = 80

#Quad vertices
A = np.array([0, 0])
C = np.array([ac, 0])
D = np.array([ad * np.cos(np.pi / 180 * angA), ad * np.sin(np.pi / 180 * angA)])
B = A + angleBisector(A, C, D) * length_of_bis 

print(A, C, B, D)

#Generating all lines
x_AC = line_gen(A, C)
x_AD = line_gen(A, D)
x_DB = line_gen(D, B)
x_BC = line_gen(B, C)
x_AB = line_gen(A, B)

#Plotting all lines
plt.plot(x_AC[0,:], x_AC[1,:], label='$AC$')
plt.plot(x_AD[0,:], x_AD[1,:], label='$AD$')
plt.plot(x_DB[0,:], x_DB[1,:], label='$DB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_AB[0,:], x_AB[1,:], linestyle='dashed', label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(0.3, 0.05, 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.02), B[1], 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.2), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

#if using termux
# plt.savefig('./figs/quad.pdf')
# plt.savefig('./figs/quad.eps')
# subprocess.run(shlex.split("termux-open ./figs/quad.pdf"))
#else
plt.show()
