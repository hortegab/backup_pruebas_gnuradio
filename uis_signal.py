import numpy as np
####################################################################################################
##                                  pulso rectangular                                             ##
####################################################################################################
def pulso_rect(ntaps,n_ones):
	x=np.zeros(ntaps)                           # crea un vector de tamano ntaps lleno de ceros
	ntaps_m= int(ntaps/2)                       # el punto medio del vector
	ntaps_i= ntaps_m-int(n_ones/2)              # el punto de inicio para los unos
	x[ntaps_i:ntaps_i+n_ones:1]=np.ones(n_ones) #llenado de los unos
	return x
