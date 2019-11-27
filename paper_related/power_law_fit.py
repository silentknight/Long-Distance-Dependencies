import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models

x = np.logspace(0.7, 2.3, 500)
f = models.SmoothlyBrokenPowerLaw1D(amplitude=2.1, x_break=10,
                                    alpha_1=0.46, alpha_2=0.008)

plt.figure()
plt.title("amplitude=1, x_break=20, alpha_1=-2, alpha_2=2")

f.delta = 0.5
plt.loglog(x, f(x), '--', label='delta=0.5')

f.delta = 0.3
plt.loglog(x, f(x), '-.', label='delta=0.3')

f.delta = 0.1
plt.loglog(x, f(x), label='delta=0.1')

plt.legend(loc='lower center')
plt.grid(True)
plt.show()