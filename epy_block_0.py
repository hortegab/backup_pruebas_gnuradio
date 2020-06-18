import numpy
from gnuradio import gr
class vec_mean_e_ff(gr.sync_block):
    """
El bloque vec_mean_e_ff recibe una senal con tramas de tamano fijo de
N valores y va entregando una trama del mismo tamano que corresponde a
la trama media de todas las tramas que va recibiendo. Los parametros usados son:
N: Es el tamano del vector o trama
Nensayos: Es el umbral que limita el numero maximo de promedios correctamente
realizados. Cuando se supera Nensayos, la trama media deja de calcularse y
se mantiene el ultimo resultado.
    """
    def __init__ (self, N=256, Nensayos=10000000):
        gr.sync_block.__init__(self, name ="vec_mean_e_ff", in_sig =[(numpy.float32, N)],out_sig =[(numpy.float32,N)])

        # Nuestras variables especificas
        self.N=N
        self.Nensayos = numpy.uint64 = Nensayos
        self.med = numpy.empty(N, dtype = numpy.float64)
        self.count = numpy.uint64 =0

    def work (self, input_items, output_items):

        # Traduccion de matrices 3D a 2D:
        in0 = input_items[0]
        #  -  input_items es una matriz 3D
        #  -  pero in0 es una matriz 2D.
        #       * Cada columna es una muestra de la senal. Hay N muestras, es constante
        #       * Cada fila es una trama de la senal. es variable

        # indentificacion del tamano L de la matriz in0
        L= in0.shape
        #  L[0] es el numero de filas = numero de tramas de senal
        #  L[1] = N es el numero de columnas = muestras de la senal en cada trama 

        out0 = output_items[0]

        # conteo de tramas procesadas y calculo de la Esperanza
        if self.count < self.Nensayos:
            self.count += L[0]

            # Esperanza de las funciones muestras ( filas de matriz ) que tiene in0 :
            mean = in0.mean(0)

            # ajuste de la Esoeranza ya calculada , con la Esperanza de in0 :
            self.med = (self.med*(self.count-L[0])+mean*L[0])/self.count

        # Entrega de resultados
        out0[:]= self.med
        return len (out0)
