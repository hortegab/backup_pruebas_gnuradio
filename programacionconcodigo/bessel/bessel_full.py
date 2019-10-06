from scipy import special
import numpy as np
import matplotlib.pyplot as plt

plt.figure()

beta = np.linspace(0,8,400)
N=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])

for k in N:
	plt.plot(beta,special.jn(k,beta),label='$J_%s$' % k, linewidth=3)

plt.legend()
plt.title('Funciones de Bessel')
plt.ylabel('$J_k$')
plt.xlabel(r'$\beta$')
plt.axhline(0, color="black")
plt.show()

