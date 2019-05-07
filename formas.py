import math
import numpy as np
# senal en forma de ventana
def ventana(Sps):
    return Sps*[1.,]
##  Forma sinc 
def sinc(Sps,ntaps):
    n=np.linspace(-int(ntaps/2), int(ntaps/2-1),ntaps)
    h=np.sinc(n/Sps)
#    return h/numpy.amax(h)
    return h
# forma diente se sierra
def saw(Sps):
    return np.linspace(0,Sps-1,Sps)	


