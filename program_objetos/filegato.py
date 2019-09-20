class Gato:
    def __init__(self, energia, alimento):
        self.energia = energia
        self.alimento = alimento
        print 'Se creo un gato'
 
    def tomar_leche(self, leche_en_litros):
        self.alimento += leche_en_litros
        print 'el gato toma su leche'
 
    def acariciar(self):
        print 'prrrrr...'
 
    def jugar(self):
        if self.energia <= 0 or self.alimento <=1:
            print 'NO QUIERO JUGAR'
        else:
            self.energia -=1
            self.alimento -= 2
            print 'al gato le encanta jugar'
 
    def dormir(self, horas):
        self.energia += horas
        print 'el gato tomo una siesta'