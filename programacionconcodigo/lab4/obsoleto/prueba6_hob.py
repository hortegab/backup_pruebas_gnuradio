# from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import numpy as np

#x_data, y_data = [], []
N=10
x_data=np.linspace(0,5.,N)
y_data = np.linspace(0,1.,N)

figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')

def update(frame):
    x_data=np.linspace(0,5.,N)
    y_data=np.random.rand(N)
    line.set_data(x_data, y_data)
    #figure.gca().relim()
    #figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=200)

pyplot.show()