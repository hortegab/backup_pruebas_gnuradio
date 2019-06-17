import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def senal(t):
	return 1 + np.sin(2 * np.pi * t/0.7)	

for T in range(1000):
	t = np.arange(T-1, T, 0.005)
	s=senal(t)
	fig, ax = plt.subplots()
	ax.plot(t, s)
	#ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
	##ax.grid()
	#fig.savefig("test.png")
	plt.show()
