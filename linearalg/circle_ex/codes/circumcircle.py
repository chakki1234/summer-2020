import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


#Quad vertices
A = np.array([6, -6])
B = np.array([3, -7])
C = np.array([3, 3])
O = circumCenter(A, B, C)
print(A, B, C, O)

#generating lines
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CA = line_gen(C, A)

#plot circle
circle1 = plt.Circle((O[0], O[1]), np.linalg.norm(A-O), color='b', fill=False)

fig, ax = plt.subplots()
ax.add_artist(circle1)
ax.set_aspect('equal', adjustable='datalim')

#plot points and lines
ax.plot(x_AB[0,:], x_AB[1,:], linestyle='dotted', label='$AB$')
ax.plot(x_BC[0,:], x_BC[1,:], linestyle='dotted', label='$BC$')
ax.plot(x_CA[0,:], x_CA[1,:], linestyle='dotted', label='$CA$')
ax.text(A[0], A[1] * (1 - 0.1), 'A')
ax.plot(A[0], A[1] , 'o')
ax.text(B[0], B[1] * (1 - 0.1), 'B')
ax.plot(B[0], B[1], 'o')
ax.text(C[0], C[1] * (1 + 0.1), 'C')
ax.plot(C[0], C[1], 'o')
ax.text(O[0], O[1] * (1 - 0.2), 'O')
ax.plot(O[0], O[1], 'o')

ax.legend(loc='best')

# if using termux
# ax.fig('./figs/circumcircle.eps')
# ax.fig('./figs/circumcircle.pdf')
# subprocess.run(shlex.split("termux-open ./figs/circumcircle.pdf"))
# else
fig.savefig('./figs/circumcircle.eps')