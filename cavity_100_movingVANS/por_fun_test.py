import numpy as np
import matplotlib.pyplot as plt



z = np.linspace(0.29, 0.31, 1000)

por = 0.8
l = 0.02
z_itf = 0.3

y = 1 -((1-por)/l)*np.abs(z_itf -z +l/2) #

plt.plot(z,y)
plt.show()
