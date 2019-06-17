import sys
from PyQt4 import QtGui

def main():
  app = QtGui.QApplication(sys.argv)

  etiqueta_hola = QtGui.QLabel("Hola Mundo!")
  etiqueta_hola.show()

  return app.exec_()

if __name__ == '__main__':
  sys.exit(main())
