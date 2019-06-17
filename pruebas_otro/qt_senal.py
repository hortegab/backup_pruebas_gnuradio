import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
  mi_senial = QtCore.pyqtSignal(Objeto)
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.entrada_texto = QtGui.QLineEdit(self)
    self.resultado_lbl = QtGui.QLabel('Resultado:', self)

    self.entrada_texto.move(0, 0)
    self.resultado_lbl.move(0,40)

    self.entrada_texto.textChanged.connect(self.calcula_suma)

    self.setGeometry(200, 200, 200, 150)
    self.setWindowTitle('Boton')
    self.show()

  def calcula_suma(self, entrada):
    resultado = "Error"
    print(entrada)
    try:
      resultado = "Resultado: " + str(eval(entrada))
    except Exception as e:
      print(e)
    self.resultado_lbl.setText(resultado)
    self.resultado_lbl.adjustSize()

def main():
  app = QtGui.QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())
if __name__ == '__main__':
  main()
