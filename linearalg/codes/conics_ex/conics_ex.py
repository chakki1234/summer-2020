import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex


# equation - 3x^2 - 4x + 20/3
X_coord_1 = np.array(np.linspace(-2.0, 4.0, num=40))
Y_coord_1 =  [3*num**2 - 4*num + 20/3 for num in X_coord_1]

# equation - x^2 - 2x + 3/2
X_coord_2 = np.array(np.linspace(-2.0, 4.0, num=40))
Y_coord_2 =  [num**2 - 2*num + 3/2 for num in X_coord_2]

# equation - 27x^2 - 10x + 1
X_coord_3 = np.array(np.linspace(-2.0, 4.0, num=300))
Y_coord_3 =  [27*num**2 - 10*num + 1 for num in X_coord_3]

# equation - 21x^2 - 28x + 10
X_coord_4 = np.array(np.linspace(-2.0, 4.0, num=100))
Y_coord_4 =  [21*num**2 - 28*num + 10 for num in X_coord_4]

#plot points and lines
plt.figure(1)
plt.plot(X_coord_1, Y_coord_1, label='$3x^2 - 4x + 20/3$')
plt.grid()
plt.legend(loc='best')
plt.axis([-10, 10, 0, 20])

plt.figure(2)
plt.plot(X_coord_2, Y_coord_2, label='$x^2 - 2x + 3/2$')
plt.grid()
plt.legend(loc='best')
plt.axis([-10, 10, 0, 8])

plt.figure(3)
plt.plot(X_coord_3, Y_coord_3, label='$27x^2 - 10x + 1$')
plt.grid()
plt.legend(loc='best')
plt.axis([-2, 2, 0, 2])
plt.savefig('./figs/quadratic_equation_3.eps')

plt.figure(4)
plt.plot(X_coord_4, Y_coord_4, label='$21x^2 - 28x + 10$')
plt.grid()
plt.legend(loc='best')
plt.axis([-5, 5, 0, 20])


# if using termux
# plt.savefig('./figs/quadratic_equation.pdf')
# plt.savefig('./figs/quadratic_equation.eps')
# subprocess.run(shlex.split("termux-open ./figs/quadratic_equation.pdf"))
# else
plt.show()
