import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    boton1 = QtGui.QPushButton('Botn1', self)
    boton2 = QtGui.QPushButton('Botn2', self)
    boton1.move(50, 50)
    self.setGeometry(300, 300, 200, 150)
    self.setWindowTitle('Botn')
    self.show()

def main():
  app = QtGui.QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
