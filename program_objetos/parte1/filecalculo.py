class Calculadora:
    def __init__(self, energia, alimento):
        self.energia = energia
        self.alimento = alimento
        print('Se creo una calculadora')
 
    def sumar(self, escala):
        y=(self.energia+self.alimento)*escala
        #self.alimento += leche_en_litros
        return y
        print('hemos sumadoe')
 
    def restar(self, escala):
        y=(self.energia-self.alimento)*escala
        #self.alimento += leche_en_litros
        print('hemos restado')
 