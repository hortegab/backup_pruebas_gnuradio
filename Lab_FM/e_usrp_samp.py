import math

# calculo de la frecuencia de muestreo para el USRP2920
def usrp2920(B):
	Kdmax=512
	samp_rate_usrp_rx=100e6
	Kdd=int(samp_rate_usrp_rx/B)
	Kda=pow(2,int(math.log(Kdd,2)))
	Kd=min(Kda,Kdmax)
	return samp_rate_usrp_rx/Kd
	
