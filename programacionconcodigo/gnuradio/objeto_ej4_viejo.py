#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Lo de arriba es para que los IDE conozcan en que esta escrito este codigo 
###########################################################
# Puedes encontrar este codigo como objeto_ej4.py en:    ##
# https://sites.google.com/saber.uis.edu.co/comdig/sw    ##
###########################################################
###           IMPORTACION DE LIBRERIAS                  ###
###########################################################
# Libreria obligatoria
from gnuradio import gr

# Librerias particulares
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes
# Librerias para poder incluir graficas tipo QT
from gnuradio import qtgui
from PyQt4 import Qt # si no se acepta PyQt4 cambie PyQt4 por PyQt5
import sys, sip

###########################################################
###           LA CLASE DE UN BLOQUE NUESTRO             ###
###########################################################
import numpy as np
from gnuradio import gr

# Se recomienda que el nombre de la clase finalice con una o dos letras especiales:
# nombre_ff: en el bloque sus entradas y salidas son senales reales y de tipo flotante
# nombre_f: solo tiene una entrada o una salida y es una senal real de tipo flotante
# En vez de "f" puden usarse: c (compleja),  i (entero), b (binario), 
# c (entero corto, de 8 bits)


class e_add_cc(gr.sync_block):  
    """Aqui debes explicar como funciona el bloque, los parametros usados.
    En este caso particular estamos definiendo nuestra propia version del bloque add"""

    # Dentro de la funcion __init__(), deben definirse los param. de config del bloque.
    # A cada param. se le da un valor por defecto, por ej  def __init__(self, amp=1.0):
    def __init__(self):
        # En la siguiente funcion debes recordar que usaras:
        # sync: cuando tu bloque sea de tipo sincrono
        # (por cada muestra entrante habra una saliente)
        # decim: cuando es un bloque decimador 
        # (por cada muestra saliente hay un numero entero de muestras entrantes)
        # interp: cuando es un bloque interpolador
        # (por cada muestra entrante hay un numero entero de muestras salientes)
        # basic: cuando no hay relacion entre el numero de muestras entrantes y salientes
        gr.sync_block.__init__(
            self,
            # Lo sig-te es define el nombre que tendra nuestro bloque para usuarios de GRC
            name='e_dd_ff', 
            # A continuacion se definen los tipos de senales de entrada. Veamos ejemplos:
            # [np.complex64]: cuando se tiene una entrada y es compleja
            # [np.float32]: cuando se tiene una entrada real de tipo flotante
            # [np.float32, np.complex64]: una entrada real flotante otra compleja
            # otros casos: int8 o byte (entero de 8 bits, que en C++ se conoce como char)
            # No hemos explorado mas casos, pero si que no es tan sencillo. 
            # Uno supondria que otros casos posibles son: int16 (en C++ se conoce como
            # short), int32, int64. Los dos primeros funcionan, pero int64 no.
            in_sig=[np.complex64,np.complex64],

            # aqui aplica lo mismo explicado anteriormente
            out_sig=[np.complex64]
        )
        # abajo se puede escribir lo que se le antoje al programador, por ejemplo:
        # self.coef=1.0: define la variable global acum y le asigna el valor cero
        # self significa que es una variable global, que se puede involcar
        # directamente desde otras fun-es. Se pueden definir las fun-es que se deseen
        # En todo caso, lo usual es que esas variables y fun-nes sean usadas en work() 
        self.coef = 1.0

    # La funcion work() es donde estara la logica del bloque 
    def work(self, input_items, output_items):
	    in0 = input_items[0]
	    in1 = input_items[1]
	    out0 = output_items[0]
	    out0[:]=(in0+in1)*self.coef
            return len(out0)

###########################################################
###           LA CLASE DEL FLUJOGRAMA                   ###
###########################################################
class flujograma(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)

        ################################################
        ###   EL FLUJOGRAMA                          ###
        ################################################

        # Las variables
        samp_rate = 1e6
        fftsize = 2048

        # Los bloques
        self.src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 0.1, 1, 0)
        self.nse = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1)
#        self.add = blocks.add_cc()
        self.add = e_add_cc()
        self.thr = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)
        self.snk = qtgui.sink_c(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )

        # Las conexiones
        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)

        # La configuracion para graficar
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()

###########################################################
###                LA CLASE PRINCIPAL                   ###
###########################################################
def main():
    # Para que lo nuestro sea considerado una aplicación tipo QT GUI
    qapp = Qt.QApplication(sys.argv)
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    # Para arranque la parte grafica
    qapp.exec_()

# como el main lo hemos puesto como una funcion, ahora hay que llamarla
# podriamos escibir simplemete main(), pero es mas profesional asi:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
