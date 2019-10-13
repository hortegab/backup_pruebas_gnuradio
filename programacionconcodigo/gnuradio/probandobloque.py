import numpy as np


def work(input_items, output_items):
	coef = 1.0
	in0 = input_items[0]
	in1 = input_items[1]
	out0 = output_items[0]
	out0[:]=(in0+in1)*coef
    	return out0

x0=np.array([1.,2.,3.,4.,5.,6.,7.,8.])
x1=np.array([1.,3.,3.,6.,5.,6.,7.,8.])
f=work(x0,x1)
print("f= ", f)