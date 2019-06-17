import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')

def lea_datos():
	dataset = open('example.txt', 'r').read()
	dataset_puro=dataset.split('\n')
	xs= []
	ys= []
	for fila in dataset_puro:
		if len(fila)> 1:
			x,y = fila.split(',')
			xs.append(x)
			ys.append(y)
	return xs,ys

def dibuje_datos(i):
	x,y=lea_datos()
	ax1.clear()
	ax1.plot(x,y)

#dibuje_datos(x,y)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ani = animation.FuncAnimation(fig, dibuje_datos, interval=1000)
plt.show()


