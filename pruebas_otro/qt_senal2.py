import sys
from PyQt4 import QtGui, QtCore

class Objeto:
  val = 99

class Ejemplo(QtGui.QWidget):
  mi_senial = QtCore.pyqtSignal(Objeto)
  def __init__(self):
      super().__init__()

      self.initUI()

  def initUI(self):

      boton_ok = QtGui.QPushButton("OK")
      boton_cancelar = QtGui.QPushButton("Cancelar")

      fuente = QtGui.QFont()
      fuente.setPixelSize(40)
      boton_ok.setFont(fuente)

      hbox = QtGui.QHBoxLayout()
      hbox.addWidget(boton_ok,0)
      hbox.addStretch(1)
      hbox.addWidget(boton_cancelar)

      vbox = QtGui.QVBoxLayout()
      vbox.addStretch(1)
      vbox.addLayout(hbox)

      self.setLayout(vbox)

      boton_ok.clicked.connect(self.emite)
      self.mi_senial.connect(self.procesa_senial)
      self.algo = Objeto()
      self.setGeometry(300, 300, 300, 150)
      self.setWindowTitle('Buttons')
      self.show()

  def emite(self):
    self.mi_senial.emit(self.algo)
  def procesa_senial(self, algo):
    print(algo, type(algo), algo.val)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Ejemplo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
